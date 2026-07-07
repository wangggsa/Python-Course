operator = input("Enter an operator (+ - * /): ")

if operator not in ["+", "-", "*", "/"]:
    print("You can only enter an operator (+ - * /)")
else:
    num1 = float(input("Enter the 1st number: "))
    num2 = float(input("Enter the 2nd number: "))

    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        result = num1 / num2

    print(f"The result is: {round(result, 3)}")