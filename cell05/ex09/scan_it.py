#!/usr/bin/env python3
import sys
args = sys.argv[1:]
if len(args) < 2:
    print("none")
else:
    a = args[0].lower()
    b = " ".join(args[1:]).lower()
    words = b.split()
    count = 0
    for i in words:
        if i == a:
            count += 1
    print(count)