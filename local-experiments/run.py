#!/usr/bin/env python3
import argparse
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).parent

def run_cmd(cmd):
    subprocess.check_call([sys.executable, str(cmd)])

def main():
    parser = argparse.ArgumentParser(description='Run local experiment scripts')
    sub = parser.add_subparsers(dest='cmd')

    sub.add_parser('cpu')
    sub.add_parser('memory')
    sub.add_parser('disk')
    sub.add_parser('kill')
    sub.add_parser('http-delay')

    args, rest = parser.parse_known_args()
    if not args.cmd:
        parser.print_help()
        sys.exit(1)

    mapping = {
        'cpu': ROOT / 'cpu_stress.py',
        'memory': ROOT / 'memory_stress.py',
        'disk': ROOT / 'disk_fill.py',
        'kill': ROOT / 'kill_process.py',
        'http-delay': ROOT / 'http_delay_client.py',
    }

    target = mapping[args.cmd]
    # forward remaining args to target script
    run_cmd([str(target)] + rest) if False else subprocess.check_call([sys.executable, str(target)] + rest)

if __name__ == '__main__':
    main()
