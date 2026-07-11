rows = int(input("Enter how many rows for your rectangle: "))
coloumns = int(input("Enter how many coloumns for your rectangle: "))
symbol = input("Enter a symbol for your rectangle: ")

for x in range(rows):
    for y in range(coloumns):
        print(symbol, end="")
    print()