# Build CLI with python's argparse

# https://realpython.com/command-line-interfaces-python-argparse/

import sys
from pathlib import Path


if (args_count := len(sys.argv)) > 2:
    print(f"One argument expected, got {args_count - 1}")
    raise SystemExit(2)

elif args_count < 2:
    print("You must specify the target directory")
    raise SystemExit(2)


target_dir = Path(sys.argv[1])

print(target_dir)

if not target_dir.is_dir():
    print("The target directory doesn't exist")
    raise SystemExit(1)

for entry in target_dir.iterdir():
    print(entry.name)