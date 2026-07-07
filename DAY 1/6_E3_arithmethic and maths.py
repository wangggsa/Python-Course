import math

depan = float(input('Masukkan panjang sisi depan segitiga (cm): '))
samping = float(input('Masukkan panjang sisi samping segitiga (cm): '))

hasil = math.sqrt(pow(depan, 2) + pow(samping, 2))

print(f'Panjang sisi miring segitiga adalah: {hasil} cm')