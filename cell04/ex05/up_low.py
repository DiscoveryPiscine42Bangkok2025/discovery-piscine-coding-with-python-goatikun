#!/usr/bin/env -S python3
a = str(input(""))
for i in a:
  j = i
  if i == j.upper():
    print(i.lower(),end = "")
  else:
    print(i.upper(), end = "")