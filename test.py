def cek_input_user(inputan):
    if(inputan==""):
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




while True:
    NAMA = input("Masukan nama : ").strip()
    if cek_input_user(NAMA)=="string":
        break
    else:
        print("Inputan tidak valid mohon ulangi")


print("Anda memasukan {inputan} {namaku}".format(inputan=cek_input_user(NAMA),namaku=NAMA))