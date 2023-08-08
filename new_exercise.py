#!/usr/bin/env python3

import os
import sys
from glob import glob

if len(sys.argv[1:]) == 0:
    raise SystemExit("filename not provided!")

next_number = len(glob("exercise*")) + 1
dir_path = f"exercise{next_number:02}"

os.makedirs(os.path.join(dir_path, "beyond"))

filename = sys.argv[1].removesuffix(".py")

with open(os.path.join(dir_path, f"{filename}.py"), mode="x") as f, open(
    os.path.join(dir_path, f"{filename}_test.py"), mode="x"
) as test:
    print(f"The files {f.name} and {test.name} was successful created!")
