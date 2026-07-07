unit = input("Is this temperature in Celcius or Fahrenheit (C/F)? ")

if unit not in ["C", "F"]:
    print(f"'{unit}' is an invalid unit of ours. Please put in either C or F.")
else:
    temp = float(input("Enter your temperature: "))

    if unit == "C":
        temp = (9 * temp) / 5 + 32
        convert_to = "Fahrenheit"
        con = "°F"
    elif unit == "F":
        temp = (temp - 32) * 5 / 9
        convert_to = "Celcius"
        con = "°C"
    
    print(f"Your temperature in {convert_to} is {round(temp, 1)} {con}.")