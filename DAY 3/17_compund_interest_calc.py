modal_awal = 0
suku_bunga = 0
periode = 0

while modal_awal <= 0 :
    modal_awal = float(input("Masukkan modal awal (Rp): "))
    if modal_awal <= 0:
        print("Modal awal tidak bisa 0 atau kurang")

while suku_bunga <= 0 :
    suku_bunga = float(input("Masukkan suku bunga (%): "))
    if suku_bunga <= 0:
        print("Suku bunga tidak bisa 0 atau kurang")

while periode <= 0 :
    periode = float(input("Masukkan periode (Tahun): "))
    if modal_awal <= 0:
        print("Periode awal tidak bisa 0 atau kurang")

hasil = modal_awal * pow(1 + suku_bunga/100, periode)

print(f"Hasil dari perhitungan bunga majemuk mu adalah Rp.{hasil:,.2f}")