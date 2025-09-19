#!/usr/bin/env python3
import sys
args = sys.argv[1:]
if not args:
    print("none")
else:
    a = args[0]
    ans = input("What was the parameter? ")
    if a == ans:
        print("Good job!")
    else:
        print("Nope, sorry...")