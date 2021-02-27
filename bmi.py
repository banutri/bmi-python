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




#ini function untuk cek inputan user
def cek_input_user(inputan):
    if(inputan==""): # jika inputan kosong maka return "kosong"
        return "kosong"
    else:
        try:
            # Konversi inputan ke integer
            val = int(inputan) # jika konversi ini berhasil ...
            return "integer" # maka return "integer" dan cukup berhenti sampai sini
        except ValueError: # Jika konversi diatas error maka lanjut ke bawah
            try:
                # Konversi inputan ke float
                val = float(inputan) # jika konversi ini berhasil ...
                return "float"  # maka return "float" dan cukup berhenti sampai sini
            except ValueError: # Jika konversi diatas error maka lanjut ke bawah
                return "string" # jika konversi diatas error semua maka return string


# Yuh mulai ngoding nya

def main():
    print("==================== BODY MASS INDEX ====================")
    print("\n")


    # Mulai input NAMA
    while True:
        NAMA = input("Masukan Nama Anda\t\t\t: ")
        if(cek_input_user(NAMA)=="string"):
            break
        else:
            print("\nInput tidak valid! mohon ulangi")


    # Mulai  input nilai tinggi badan
    while True:
        tinggi_badan = input("Masukan Tinggi Badan dalam cm : ") # Ini tahap input tinggi badan kemudian dimasukan ke variable tinggi_badan
        if(cek_input_user(tinggi_badan)=="integer" or cek_input_user(tinggi_badan)=="float"):
            break
        else:
            print("\nInput tidak valid! mohon ulangi")

    # Mulai input berat badan
    while True:
        berat_badan = input("Masukan Berat Badan dalam kg  : ") # Ini tahap input berat badan kemudian dimasukan ke variable berat_badan
        if(cek_input_user(berat_badan)=="integer" or cek_input_user(berat_badan)=="float"):
            break
        else:
            print("\nInput tidak valid! mohon ulangi")

    print("\n")

    # Mulai konversi string ke float atau pecahan supaya dapat dikalkulasi
    tinggi_badan = float(tinggi_badan)
    berat_badan = float(berat_badan)

    # Mulai membagi tinggi badan dengan 100
    tinggi_badan = tinggi_badan/100

    # Mulai menghitung BMI
    indeks = berat_badan/(tinggi_badan*tinggi_badan)

    # Mulai pembulatan bilangan indeks
    indeks = round(indeks)

    # Mulai mencocokkan kategori dari hasil hitungan BMI


    if(indeks<17.0):
        print("{NAMA} mendapat indeks : {indeks:.2f}, {NAMA} masuk kategori 'Sangat Kurus'".format(NAMA=NAMA,indeks=indeks))

    elif(indeks>=17.0 and indeks <=18.40):
        print("{NAMA} mendapat indeks : {indeks:.2f}, {NAMA} masuk kategori 'Kurus'".format(NAMA=NAMA,indeks=indeks))

    elif(indeks>=18.5 and indeks<=25.0):
        print("{NAMA} mendapat indeks : {indeks:.2f}, {NAMA} masuk kategori 'Ideal atau Normal'".format(NAMA=NAMA,indeks=indeks))

    elif(indeks>=25.1 and indeks<=27.0):
        print("{NAMA} mendapat indeks : {indeks:.2f}, {NAMA} masuk kategori 'Gemuk'".format(NAMA=NAMA,indeks=indeks))

    elif(indeks>27.0):
        print("{NAMA} mendapat indeks : {indeks:.2f}, {NAMA} masuk kategori 'Sangat Gemuk atau Obesitas'".format(NAMA=NAMA,indeks=indeks))


    print("\t")

main() # Menjalankan program utama
while True:
    konfirmasi = input("Apakah ingin mengulangi? Y/N : ")
    if(konfirmasi=="Y" or konfirmasi=="y"):
        main()
    else:
        input("\nTekan sembarang tombol untuk keluar")
        break