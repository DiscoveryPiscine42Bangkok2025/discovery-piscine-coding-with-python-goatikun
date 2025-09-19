#!/usr/bin/env python3
import sys
words = sys.argv[1:]
if len(words) < 2:
    print("none")
else:
    for w in reversed(words):
        print(w, end = " ")