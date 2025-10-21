import asyncio
import sys

async def run_cmd(cmd_args):
    proc = await asyncio.create_subprocess_exec(
        *cmd_args,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE
    )
    out, err = await proc.communicate()
    return out.decode(), err.decode(), proc.returncode

async def main(target):
    print("Test run for target:", target)
    out, err, rc = await run_cmd(["echo", f"running pipeline for {target}"])
    print("OUT:", out.strip())

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python core/orchestrator.py <target>")
        sys.exit(1)
    target = sys.argv[1]
    asyncio.run(main(target))
