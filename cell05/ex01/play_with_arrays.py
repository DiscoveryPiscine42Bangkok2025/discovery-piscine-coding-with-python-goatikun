#!/usr/bin/env -S python3
from array import array
num = array('i',[2, 8, 9, 48, 8, 22, -12, 2])
print("Original array: ",num.tolist())
for idx in range(len(num)):
    num[idx] += 2
print("New array: ",num.tolist())