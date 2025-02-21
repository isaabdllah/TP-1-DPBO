from Petshop import Petshop

def main():
    shop = Petshop()
    
    while True:
        print("\n===== PetShop Management =====")
        print("1. Tampilkan Produk")
        print("2. Tambah Produk")
        print("3. Edit Produk")
        print("4. Hapus Produk")
        print("5. Cari Produk")
        print("6. Keluar")
        
        pilihan = input("Pilih menu (1-6): ")
        
        if pilihan == "1":
            shop.tampilkan_produk()
        elif pilihan == "2":
            temp_id = input("Masukkan ID produk: ")
            temp_nama = input("Masukkan nama produk: ")
            temp_kategori = input("Masukkan kategori produk: ")
            temp_harga = input("Masukkan harga produk: ")
            shop.tambah_produk(temp_id, temp_nama, temp_kategori, temp_harga)
        elif pilihan == "3":
            nama = input("Masukkan nama produk yang ingin diedit: ")
            temp_id = input("Masukkan ID baru: ")
            temp_nama = input("Masukkan nama baru: ")
            temp_kategori = input("Masukkan kategori baru: ")
            temp_harga = input("Masukkan harga baru: ")
            shop.edit_produk(nama, temp_id, temp_nama, temp_kategori, temp_harga)
        elif pilihan == "4":
            nama = input("Masukkan nama produk yang ingin dihapus: ")  # Tambahkan input nama
            shop.hapus_produk(nama)  # Panggil metode dengan parameter nama
        elif pilihan == "5":
            nama = input("Masukkan nama produk yang ingin dicari: ")
            shop.cari_produk(nama)
        elif pilihan == "6":
            print("Terima kasih telah menggunakan PetShop Management!")
            break
        else:
            print("Pilihan tidak valid, silakan coba lagi.")

if __name__ == "__main__":
    main()
