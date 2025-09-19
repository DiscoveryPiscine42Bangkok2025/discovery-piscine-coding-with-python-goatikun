#!/usr/bin/env python3
import sys
args = sys.argv[1:]
if not args:
    print("none")
else:
    for i in args:
        if not i.endswith("ism"):
            print(i + "ism")