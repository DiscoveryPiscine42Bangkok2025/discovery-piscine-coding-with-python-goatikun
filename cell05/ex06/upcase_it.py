#!/usr/bin/env -S python3
s = str(input("")) 
words = s.split()   
if s == " ":
 print("none")
else:
  for a in words:
    print(a.upper(),end = " ")