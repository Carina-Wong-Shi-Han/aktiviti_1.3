# Atur cara mengira luas permukaan isipadu silinder
# Isytihar pemalar
pi = 3.142

# Input
jejari = float(input("Masukkan jejari:"))
tinggi = float(input("Masukkan tinggi:"))

# Proses
luas_permukaan = (2 * pi* jejari * jejari )+(2 *pi * jejari * tinggi)
isipadu = pi * jejari * jejari * tinggi

# Output
print("Jumlah luas permukaan tangki air  ialah", round(luas_permukaan,2))
print("Isipadu tangki air ialah", round(isipadu,2))
