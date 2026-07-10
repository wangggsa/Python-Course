price1 = 30000.14159
price2 = -9870
price3 = 1200.34

# fixed decimal places
print(f"Price 1 is ${price1:.2f}")
print(f"Price 3 is ${price3:.2f}")
print(f"Price 2 is ${price2:.2f}")

# allocate spaces
print(f"Price 1 is ${price1:10}")
print(f"Price 2 is ${price2:10}")
print(f"Price 3 is ${price3:10}")

# allocate and 0 pad that many spaces
print(f"Price 1 is ${price1:010}")
print(f"Price 2 is ${price2:010}")
print(f"Price 3 is ${price3:010}")

# left justify
print(f"Price 1 is ${price1:<}")
print(f"Price 2 is ${price2:<}")
print(f"Price 3 is ${price3:<}")

# right justify
print(f"Price 1 is ${price1:>30}")
print(f"Price 2 is ${price2:>30}")
print(f"Price 3 is ${price3:>30}")

# center align
print(f"Price 1 is ${price1:^10}")
print(f"Price 2 is ${price2:^10}")
print(f"Price 3 is ${price3:^10}")

# for any positive number will be added a +
print(f"Price 1 is ${price1:+}")
print(f"Price 2 is ${price2:+}")
print(f"Price 3 is ${price3:+}")

# for any positive number will be added a space
print(f"Price 1 is ${price1: }")
print(f"Price 2 is ${price2: }")
print(f"Price 3 is ${price3: }")

# will be adding , every 3 digit
print(f"Price 1 is ${price1:,}")
print(f"Price 2 is ${price2:,}")
print(f"Price 3 is ${price3:,}")

print(f"Price 1 is ${price1:+,.2f}")
print(f"Price 2 is ${price2:+,.2f}")
print(f"Price 3 is ${price3:+,.2f}")