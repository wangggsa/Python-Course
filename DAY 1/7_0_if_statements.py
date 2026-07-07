age = int(input('Enter your age: '))

if age <= 0:
    print('You have not been born yet!')
elif age >= 100:
    print('WOW! How are you still alive?')
elif age >= 18:
    print('You are eligible to make an ID')
else:
    print('You must be 18+ to make an ID')