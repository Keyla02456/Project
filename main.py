from data import data_produk
from linkedlist import LinkedList

# Membuat Linked List
linked_list = LinkedList()

# Memasukkan data awal ke Linked List
for produk in data_produk:
    linked_list.tambah(produk)


# 1. Menampilkan Array/List
def tampil_array():
    print("\n=== DATA PRODUK TOKO KUE ===")

    if len(data_produk) == 0:
        print("Data kosong")
        return

    for produk in data_produk:
        print(
            produk[0],
            "-",
            produk[1],
            "- Rp",
            produk[2],
            "- Stok:",
            produk[3]
        )


# 2. Menampilkan Linked List
def tampil_linked_list():
    print("\n=== LINKED LIST ===")
    linked_list.tampil()


# 3. Menambah Data
def tambah_data():
    print("\n=== TAMBAH DATA ===")

    kode = input("Kode produk : ")
    nama = input("Nama produk : ")
    harga = int(input("Harga       : "))
    stok = int(input("Stok        : "))

    produk_baru = [kode, nama, harga, stok]

    # Masukkan ke Array/List
    data_produk.append(produk_baru)

    # Masukkan ke Linked List
    linked_list.tambah(produk_baru)

    print("Data berhasil ditambahkan!")


# 4. Edit Data
def edit_data():
    print("\n=== EDIT DATA ===")

    kode = input("Masukkan kode produk: ")

    for produk in data_produk:

        if produk[0] == kode:

            print("\nData lama:")
            print("Kode  :", produk[0])
            print("Nama  :", produk[1])
            print("Harga :", produk[2])
            print("Stok  :", produk[3])

            print("\nMasukkan data baru:")

            produk[1] = input("Nama baru  : ")
            produk[2] = int(input("Harga baru : "))
            produk[3] = int(input("Stok baru  : "))

            print("Data berhasil diedit!")
            return

    print("Data tidak ditemukan.")


# 5. Mencari Data
def cari_data():
    print("\n=== CARI DATA ===")

    kode = input("Masukkan kode produk: ")

    for produk in data_produk:

        if produk[0] == kode:

            print("\nData ditemukan!")
            print("Kode  :", produk[0])
            print("Nama  :", produk[1])
            print("Harga :", produk[2])
            print("Stok  :", produk[3])

            return

    print("Data tidak ditemukan.")


# 6. Menghapus Data
def hapus_data():
    print("\n=== HAPUS DATA ===")

    kode = input("Masukkan kode produk: ")

    for produk in data_produk:

        if produk[0] == kode:

            # Hapus dari Array/List
            data_produk.remove(produk)

            # Hapus dari Linked List
            linked_list.hapus(kode)

            print("Data berhasil dihapus!")
            return

    print("Data tidak ditemukan.")


# Menu utama
def menu():

    while True:

        print("\n==============================")
        print("       KATALOG TOKO KUE")
        print("==============================")
        print("1. Tampilkan Array/List")
        print("2. Tampilkan Linked List")
        print("3. Tambah Data")
        print("4. Edit Data")
        print("5. Cari Data")
        print("6. Hapus Data")
        print("7. Keluar")
        print("==============================")

        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            tampil_array()

        elif pilihan == "2":
            tampil_linked_list()

        elif pilihan == "3":
            tambah_data()

        elif pilihan == "4":
            edit_data()

        elif pilihan == "5":
            cari_data()

        elif pilihan == "6":
            hapus_data()

        elif pilihan == "7":
            print("Program selesai.")
            break

        else:
            print("Pilihan tidak tersedia.")


menu()