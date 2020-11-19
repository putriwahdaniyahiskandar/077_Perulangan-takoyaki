
print("Selamat Datang Di Toko Takoyaki PWI")
print("=======================================")


print("Menu Takoyaki")
print("1. varian 1 = Rp.2000/pcs")
print("2. varian 2 = Rp.2500/pcs")

pilih = int(input("Varian yg anda pesan = "))
if pilih == 1:
    harga = 2000
    jumlah = int(input("Jumlah yg anda pesan = "))
    if jumlah >= 10:
        harga_asli = harga*jumlah
        print("Kamu Membeli Lebih Dari 10pcs Varian 1")
        print("Kamu Dapat diskon 10%")
        print(" ")
        total_belanja = harga*jumlah
        diskon = total_belanja * 10/100 #10%
        bayar = total_belanja - diskon
        print("Total Harga Sebelum Discon Rp.%s"% harga_asli)
        print("Total Harga Setelah Discon Rp.%s"% bayar)
        print(" ")
        print("Total yang harus dibayar: Rp.%s" % bayar)
        print("Terima kasih sudah berbelanja")
        
    else:
        print("Kamu Memilih Varian %s"% pilih)
        print("Dengan Jumlah %s"% jumlah)
        print(" ")
        bayar = harga*jumlah
        print("Total yang harus dibayar: Rp.%s" % bayar)
        print("Terima kasih sudah berbelanja")
        
elif pilih == 2:
    harga = 2500
    jumlah = int(input("Jumlah yg anda pesan = "))
    if jumlah >= 10:
        harga_asli = harga*jumlah
        print("Kamu Membeli Lebih Dari 10pcs Varian 2")
        print("Kamu Dapat diskon 8%")
        print(" ")
        total_belanja = harga*jumlah
        diskon = total_belanja * 8/100 #10%
        bayar = total_belanja - diskon
        print("Total Harga Sebelum Discon Rp.%s"% harga_asli)
        print("Total Harga Setelah Discon Rp.%s"% bayar)
        print(" ")
        print("Total yang harus dibayar: Rp.%s" % bayar)
        print("Terima kasih sudah berbelanja")
        
    else:
        print("Kamu Memilih Varian %s"% pilih)
        print("Dengan Jumlah %s"% jumlah)
        print(" ")
        bayar = harga*jumlah
        print("Total yang harus dibayar: Rp.%s" % bayar)
        print("Terima kasih sudah berbelanja")

else:
    print("PILIHAN TIDAK ADA")
        
print("=======================================")
print("Datang lagi yaa...")
print("=======================================")