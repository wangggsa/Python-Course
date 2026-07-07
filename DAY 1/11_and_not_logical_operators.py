temp = 20
is_sunny = False

if temp >= 32 and is_sunny:
    print("It is HOT outside.")
    print("And it is SUNNY")
elif temp <= 16 and is_sunny:
    print("It is COLD outside.")
    print("And it is SUNNY")
elif 30 > temp > 16 and is_sunny:
    print("It is WARM outside")
    print("And it is SUNNY")
elif temp >= 32 and not is_sunny:
    print("It is HOT outside.")
    print("And it is CLOUDY")
elif temp <= 16 and not is_sunny:
    print("It is COLD outside.")
    print("And it is CLOUDY")
elif 30 > temp > 16 and not is_sunny:
    print("It is WARM outside")
    print("And it is CLOUDY")