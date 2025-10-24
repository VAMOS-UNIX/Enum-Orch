import argparse
from core.orchestrator import Orchestrator

def parse_args():
    p = argparse.ArgumentParser(prog="enum-orch", description="Enum-Orch - orchestration tool")
    p.add_argument("-t", "--target", required=True, help="Target IP or hostname")
    p.add_argument("-o", "--outdir", default="data", help="Output directory")
    return p.parse_args()

def main():
    args = parse_args()
    orch = Orchestrator(outdir=args.outdir)
    orch.run([args.target])

if __name__ == "__main__":
    main()
