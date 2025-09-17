num1 = str(input(" "))
num2 = str(input(" "))
if num1.strip() == "" or num2.strip() == "":
    print("none")
else:
  words = range(int(num1),int(num2)+1)
  print(list(words))