# Enum-Orch

Orchestrator for CTF enumeration — a plugin-based pipeline that runs Nmap → web fuzzers (ffuf/feroxbuster) and normalizes results as JSON.

## Warning
Only use against systems you own or have explicit permission to test. Unauthorized scanning is illegal.

## Requirements
- Python 3.10+
- nmap
- ffuf (optional)

## Quickstart
```bash
git clone https://github.com/<yourname>/Enum-Orch.git
cd Enum-Orch
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python core/orchestrator.py --target 127.0.0.1
```
