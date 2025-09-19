#!/usr/bin/env python3
import sys
words = sys.argv[1:]
if not words:
    print("none")
else:
    for w in words:
        print(w.upper(), end = " ")