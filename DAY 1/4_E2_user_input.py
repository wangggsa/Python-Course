# EXERCISE 2
item = input('What would u like to buy? ')
price = float(input('What is the price of your item? '))
quantity = int(input('How much is your item? '))

total = price * quantity

print(f'Your have bought {quantity} x {item}/s, and the total is ${total}')