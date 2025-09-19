#!/usr/bin/env python3
import sys
args = sys.argv[1:]
if len(args) < 2:
    print("none")
else:
    num1 = args[0].strip()
    num2 = args[1].strip()
    if not num1 or not num2:
        print("none")
    else:
        try:
            start = int(num1)
            end = int(num2)
            words = range(start, end + 1)
            print(list(words))
        except ValueError:
            print("none")