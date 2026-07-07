weight = float(input("Enter your weight: "))
unit = input("Kilograms or pounds (K / L): ")

if unit not in ["K", "L"]:
    print(f"'{unit}' was not a valid unit. Please input either K or L !!!")
else:
    if unit == "K":
        weight = weight * 2.205
        unit = "Lbs"
    elif unit == "L":
        weight = weight / 2.205
        unit = "Kgs"
    print(f"Your weight is {round(weight, 1)} {unit}")