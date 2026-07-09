username = input("Enter your username: ")

if len(username) > 12:
    print("Your username could'nt contain more than 12 characters")
elif not username.find(" ") == -1:
    print("Your username could'nt contain any space/s")
elif not username.isalpha():
    print("Your username could'nt contain any digit/s")
else:
    print(f"Your username is PERFECT!, Welcome {username}")