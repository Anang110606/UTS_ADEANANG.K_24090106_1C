# Program kalkulator BMI

# Input berat badan
weight = float(input("Masukkan Berat Badan (Kg): "))

# Input tingi badan
height = float(input("Masukkan Tinggi Badan (M): "))

# kalkulator BMI
bmi = weight / (height ** 2)

# Determine BMI 
if bmi < 18.5:
    category = "Berat badan kurang"
elif 18.5 <= bmi < 24.9:
    category = "Berat badan normal"
elif 25 <= bmi < 29.9:
    category = "Kelebihan berat badan"
else:
    category = "Obesitas"

# Display the results
print("\nBerat Badan     : {:.2f} Kg".format(weight))
print("Tinggi Badan    : {:.2f} M".format(height))
print("Nilai BMI Anda  : {:.2f}".format(bmi))
print("Kategori BMI    : {}".format(category))
