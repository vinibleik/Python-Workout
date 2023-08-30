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

filenames_list = [
    os.path.join(dir_path, f"{filename}.py"),
    os.path.join(dir_path, f"test_{filename}.py"),
    os.path.join(dir_path, "beyond", "beyond.py"),
    os.path.join(dir_path, "beyond", "test_beyond.py"),
]

for file in filenames_list:
    with open(file, mode="x") as f:
        print(f"{f.name} was successful creates!")
