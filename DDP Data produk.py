# PENGELOLAAN DATA PRODUK

# DATA PRODUK
produk = {
    "nama": "Pulpen",
    "harga": 5000,
    "stok": 20
}

print("DATA PRODUK AWAL")
print(produk)


# MENU PENGELOLAAN DATA
while True:
    print("MENU PENGELOLAAN DATA")
    print("1. Tampilkan Data")
    print("2. Tambah Kategori")
    print("3. Ubah Harga")
    print("4. Hapus Kategori")
    print("5. Keluar")

    pilihan = input("Pilih Menu : ")


    # MENAMPILKAN DATA PRODUK
    if pilihan == "1":
        print("DATA PRODUK")
        print("Nama     :", produk["nama"])
        print("Harga    :", produk["harga"])
        print("Stok     :", produk["stok"])

        if "kategori" in produk:
            print("Kategori :", produk["kategori"])


    #  MENAMBAHKAN KATEGORI
    elif pilihan == "2":
        kategori = input("Masukkan kategori : ")
        produk["kategori"] = kategori

        print("Kategori berhasil ditambahkan.")
        print("Data produk terbaru :", produk)


    # MENGUBAH HARGA
    elif pilihan == "3":
        harga_baru = int(input("Masukkan harga baru : "))
        produk["harga"] = harga_baru

        print("Harga berhasil diubah.")
        print("Data produk terbaru :", produk)


    # MENGHAPUS KATEGORI
    elif pilihan == "4":
        if "kategori" in produk:
            produk.pop("kategori")

            print("Kategori berhasil dihapus.")
            print("Data produk terbaru :", produk)
        else:
            print("Kategori belum ada.")


    # KELUAR DARI MENU PENGELOLAAN DATA
    elif pilihan == "5":
        print("Program selesai.")
        break


# DATA AKHIR
print("DATA PRODUK AKHIR")
print(produk)