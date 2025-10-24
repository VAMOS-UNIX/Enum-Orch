import asyncio
import sys
import json
import os
from plugins.eo_nmap import NmapPlugin


class Orchestrator:
    def __init__(self, outdir="data"):
        self.outdir = outdir
        os.makedirs(self.outdir, exist_ok=True)
        # You can add additional plugins here later.
        self.plugins = {
            "nmap": NmapPlugin(),
            # "ffuf": FfufPlugin(), ...
        }

    async def run_target(self, target: str):
        print(f"[orch] start: {target}")
        results = {}
        nmap = self.plugins.get("nmap")
        if nmap:
            try:
                nmap_findings = await nmap.run(target)
            except Exception as e:
                nmap_findings = [{"target": target, "tool": "nmap", "error": f"exception: {e}"}]
            results["nmap"] = nmap_findings
            out_path = os.path.join(self.outdir, f"{target}-nmap.json")
            with open(out_path, "w") as f:
                json.dump(nmap_findings, f, indent=2)
            print(f"[orch] nmap results saved -> {out_path}")
        else:
            print("[orch] no nmap plugin found")

        print(f"[orch] done: {target}")
        return results

    def run(self, targets):
        asyncio.run(self._run_many(targets))

    async def _run_many(self, targets):
        tasks = [self.run_target(t) for t in targets]
        await asyncio.gather(*tasks)