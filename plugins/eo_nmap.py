import asyncio
import xml.etree.ElementTree as ET
from plugins.base import Plugin
import shlex
import os

class NmapPlugin(Plugin):
    name = "nmap"

    async def run(self, target: str):
        cmd = ["nmap", "-Pn", "-sS", "-sV", "-p", "1-65535", "--min-rate", "500", "-oX", "-", target]
        proc = await asyncio.create_subprocess_exec(*cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE)
        out, err = await proc.communicate()
        out_text = out.decode(errors="ignore")
        findings = []
        try:
            root = ET.fromstring(out_text)
            for host in root.findall("host"):
                for ports in host.findall("ports"):
                    for port in ports.findall("port"):
                        state = port.find("state").get("state")
                        if state != "open":
                            continue
                        pnum = int(port.get("portid"))
                        proto = port.get("protocol")
                        service = port.find("service")
                        svcname = service.get("name") if service is not None else ""
                        findings.append({
                            "target": target,
                            "tool": "nmap",
                            "port": pnum,
                            "proto": proto,
                            "service": svcname,
                            "raw": "" 
                        })
        except Exception:
            findings.append({"target": target, "tool": "nmap", "error": "parse_failed", "raw": out_text[:1000]})
        return findings
