# Cara hitung BMI itu
# tinggi badan dalam cm dibagi 100 dulu. misal 165cm / 100 = 1,65
# lalu tinggi badan dipangkat 2 atau 1,65x1,65
# setelah itu berat badan dibagi dengan hasil dari pangkat tinggi badan yang tadi
# misal, tinggi badan 165cm dan berat badan 75kg
# hitungan nya adalah. 75/(1,65x1,65) = 27,55
# setelah mendapatkan hasil hitungan nya, kemudian hasil dicocokkan dengan kategori BMI
# Kategori : 
# Di bawah 17,0 = Kurus, kekurangan berat badan berat
# 17,0 - 18,4 = Kurus, kekurangan berat badan ringan
# 18,5 – 25,0 = Normal
# 25,1 – 27,0 = Gemuk
# Lebih dari 27 = Gemuk, kelebihan berat badan tingkat berat atau obesitas


# Yuh mulai ngoding nya


# Mulai  input nilai tinggi badan dan berat badan
tinggi_badan = float(input("Masukan tinggi badan dalam cm : ")) # Ini tahap input tinggi badan tipe float kemudian dimasukan ke  variable tinggi_badan

berat_badan = float(input("Masukan berat badan dalam kg : ")) # Ini tahap input berat badan tipe float kemudian dimasukan ke  variable berat_badan


# Mulai membagi tinggi badan dengan 100
tinggi_badan = tinggi_badan/100


# Mulai menghitung BMI
indeks = berat_badan/(tinggi_badan*tinggi_badan)



# Mulai mencocokkan kategori dari hasil hitungan BMI
if(indeks<17.0):
    print("Anda mendapat indeks : {:.2f}, anda masuk kategori 'Sangat Kurus'".format(indeks))

elif(indeks>=17.0 and indeks <=18.4):
    print("Anda mendapat indeks : {:.2f}, anda masuk kategori 'Kurus'".format(indeks))

elif(indeks>=18.5 and indeks<=25.0):
    print("Anda mendapat indeks : {:.2f}, anda masuk kategori 'Ideal atau Normal'".format(indeks))

elif(indeks>=25.1 and indeks<=27.0):
    print("Anda mendapat indeks : {:.2f}, anda masuk kategori 'Gemuk'".format(indeks))

elif(indeks>27.0):
    print("Anda mendapat indeks : {:.2f}, anda masuk kategori 'Sangat Gemuk atau Obesitas'".format(indeks))
