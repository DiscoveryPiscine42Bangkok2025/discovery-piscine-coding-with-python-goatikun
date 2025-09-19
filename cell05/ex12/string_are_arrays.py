#!/usr/bin/env -S python3
import sys
args = sys.argv[1:]
if not args:
    print("none")
else:
    a = " ".join(args)
    ans = ''
    for i in a:
        if i == 'z':
            ans += 'z'
    if not ans:
        print("none")
    else:
        print(ans)