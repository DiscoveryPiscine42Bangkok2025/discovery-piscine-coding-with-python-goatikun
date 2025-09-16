num1 = int(input("Enter the first number :"))
num2 = int(input("Enter the second number :"))

multnum = num1 * num2
print(f"{num1} x {num2} = {multnum}")

if multnum == 0 :
    print("This number is both positive and negative")
elif multnum > 0 :
    print("This number is positive.")
else :
    print("This number is negative.")