#!/usr/bin/env -S python3
s = str(input("")) 
words = s.split() 
if s == " ":
 print("none")
elif len(words) < 2:
  print("none")
else:
  i = len(words)-1
  for a in range(0,len(words)):
    print(words[i],end = " ")
    i = i-1