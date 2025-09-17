num = 0 
while (num < 11):
    multi = 0
    print(f"Table de {num} : ",end = " ")
    while multi < 11:
        result = num * multi
        print(result,end = " ")
        multi += 1
    num += 1
    print()