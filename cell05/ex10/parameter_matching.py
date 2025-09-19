#!/usr/bin/env -S python3
a = str(input(" "))
if a == " ":
  print("none")
else:
  ans = str(input("What was the parameter? "))
  if a == ans:
    print("Good job!")
  else:
    print("Nope, sorry...")