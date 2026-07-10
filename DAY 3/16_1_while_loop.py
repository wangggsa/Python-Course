age = int(input("Enter your age: "))

while age < 1:
    print("You CAN NOT fill your age below 1yr old")
    age = int(input("Enter your age: "))
print(f"Your are {age} year/s old")