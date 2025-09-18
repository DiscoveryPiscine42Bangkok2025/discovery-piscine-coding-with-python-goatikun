#!/usr/bin/env -S python3
age = int(input("Please tell me your age : "))
print(f"You are currently {age} years old.")
i = 0
while i < 30:
    i += 10
    nextage = age + i
    print(f"In {i} years, you'll be {nextage} years old.")
    