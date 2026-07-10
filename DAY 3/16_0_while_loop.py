name = input("Enter your name: ")

while name == "":
    print("You DID NOT enter your name")
    name = input("Enter your name: ")
print(f"Hello {name}")