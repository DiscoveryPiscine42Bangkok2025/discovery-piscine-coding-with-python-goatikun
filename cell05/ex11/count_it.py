#!/usr/bin/env python3
import sys
args = sys.argv[1:]
if not args:
    print("none")
else:
    print(f"parameters: {len(args)}")
    for i in args:
        print(f"{i} : {len(i)}")