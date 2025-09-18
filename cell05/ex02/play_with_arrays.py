#!/usr/bin/env -S python3
from array import array
arr1 = array('i',[2, 8, 9, 48, 8, 22, -12, 2])
arr2 = array('i', (x + 2 for x in arr1 if x > 5))
print(arr1.tolist())
print(arr2.tolist())