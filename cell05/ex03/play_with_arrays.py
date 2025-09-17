arr = [2, 8, 9, 48, 8, 22, -12, 2]
print(arr)
unique_arr = []
for i in arr:
    if i not in unique_arr:
        unique_arr.append(i)
print(unique_arr)