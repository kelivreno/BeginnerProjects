num1 = float(input("Enter first number: "))
op = input("Enter an operator: ")
num2 = float(input("Enter second number: "))
# float(input(prompt))) converts the value in input into an integer
if op == "x":
    print(num1*num2)
elif op == "+":
    print(num1+num2)
elif op == "-":
    print(num1-num2)
elif op == "/":
    print(num1/num2)
else:
    print("invalid operator")
