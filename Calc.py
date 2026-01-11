num1 = float(input("What is the first number you want >"))
num2 = float(input("what is the second number you want >"))
function = input("Would you like to add, subtract, divide, exponentiate, multiply or use long division? >")
if function == "add":
    print(num1 + num2)
if function == "subtract":
    print(num1 - num2)
if function == "divide":
    print(num1 / num2)
if function == "multiply":
    print(num1 * num2)
if function == "exponentiate":
    print(num1 ** num2)
if function == "long division":
    print(num1 // num2)
    print(num1 % num2)