num = float(input("Enter a number between 1 - 10: "))

while not 0 < num < 11:
    print(f"'{num}' is not valid, enter a number between 1 - 10")
    num = float(input("Enter another number between 1 - 10: "))
print(f"You picked {num}")