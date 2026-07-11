# collection = single "variable" used to store multiple values
# List = [] ordered and changeable. Duplicates OK
# Set = {} unordered and immutable, but Add/Remove OK. NO duplicates
# Tuple() ordered and unchangeable. Duplicates OK. FASTER

fruits = ["orange", "apple", "coconut", "banana"]
# print(dir(fruits))
# print(help(fruits))
# print(len(fruits))
# print("apple" in fruits)

# fruits[3] = "pineapple" changes value within the string
# fruits.append("pineapple") adds new variable within the string
# fruits.remove("apple") removes variable within the string
# fruits.insert(3, "pineapple") insert a variable to specific line of string
# fruits.sort() sorts string within the alphabetical order
# fruits.reverse() reverse the variable within the string can be comboed with sort()
# fruits.clear() clears the string
# print(fruits.index("apple")) finds the index of specific variable
# print(fruits.count("pineapple")) counts a specific variable

# print(fruits[::-1])
for fruit in fruits:
    print(fruit)