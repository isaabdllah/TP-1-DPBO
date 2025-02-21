class Petshop:
    def __init__(this):
        this.id = []
        this.nama_produk = []
        this.kategori_produk = []
        this.harga_produk = []
        this.jumlah_produk = 0
    
    def __del__(this):
        pass

    # Getter & Setter
    def get_id(this, index):
        return this.id[index]
    
    def set_id(this, index, value):
        this.id[index] = value
    
    def get_nama_produk(this, index):
        return this.nama_produk[index]
    
    def set_nama_produk(this, index, value):
        this.nama_produk[index] = value
    
    def get_kategori_produk(this, index):
        return this.kategori_produk[index]
    
    def set_kategori_produk(this, index, value):
        this.kategori_produk[index] = value
    
    def get_harga_produk(this, index):
        return this.harga_produk[index]
    
    def set_harga_produk(this, index, value):
        this.harga_produk[index] = value
    
    def get_jumlah_produk(this):
        return this.jumlah_produk
    
    def longest_id(this):
        return max((len(str(i)) for i in this.id), default=3)
    
    def longest_nama(this):
        return max((len(nama) for nama in this.nama_produk), default=4)
    
    def longest_kategori(this):
        return max((len(kategori) for kategori in this.kategori_produk), default=8)
    
    def longest_harga(this):
        return max((len(str(harga)) for harga in this.harga_produk), default=5)
    
    def tampilkan_produk(this):
        if this.jumlah_produk == 0:
            print("Data kosong, tidak ada produk di PetShop!")
            return
        
        id_width = max(3, this.longest_id())
        nama_width = max(4, this.longest_nama())
        kategori_width = max(8, this.longest_kategori())
        harga_width = max(5, this.longest_harga())
        
        print("+" + "-" * (id_width + 2) + "+" + "-" * (nama_width + 2) + "+" + "-" * (kategori_width + 2) + "+" + "-" * (harga_width + 2) + "+")
        print(f"| {'ID':<{id_width}} | {'Nama':<{nama_width}} | {'Kategori':<{kategori_width}} | {'Harga':<{harga_width}} |")
        print("+" + "-" * (id_width + 2) + "+" + "-" * (nama_width + 2) + "+" + "-" * (kategori_width + 2) + "+" + "-" * (harga_width + 2) + "+")
        
        for i in range(this.jumlah_produk):
            print(f"| {this.id[i]:<{id_width}} | {this.nama_produk[i]:<{nama_width}} | {this.kategori_produk[i]:<{kategori_width}} | {this.harga_produk[i]:<{harga_width}} |")
        
        print("+" + "-" * (id_width + 2) + "+" + "-" * (nama_width + 2) + "+" + "-" * (kategori_width + 2) + "+" + "-" * (harga_width + 2) + "+")
    
    def tambah_produk(this, temp_id, temp_nama, temp_kategori, temp_harga):
        if this.jumlah_produk >= 100:
            print("PetShop sudah penuh, tidak bisa menambah produk lagi!")
            return
        
        if temp_id in this.id:
            print(f"Produk dengan ID {temp_id} sudah ada! Gagal menambahkan produk.")
            return
        
        this.id.append(temp_id)
        this.nama_produk.append(temp_nama)
        this.kategori_produk.append(temp_kategori)
        this.harga_produk.append(temp_harga)
        this.jumlah_produk += 1
        print("Produk berhasil ditambahkan!")
    
    def edit_produk(this, nama, temp_id, temp_nama, temp_kategori, temp_harga):
        if this.jumlah_produk == 0:
            print("Tidak ada produk untuk diedit!")
            return
        
        for i in range(this.jumlah_produk):
            if this.nama_produk[i] == nama:
                this.id[i] = temp_id
                this.nama_produk[i] = temp_nama
                this.kategori_produk[i] = temp_kategori
                this.harga_produk[i] = temp_harga
                print("Produk berhasil diperbarui!")
                return
        print("Produk tidak ditemukan!")
    
    def hapus_produk(this, nama):
        if this.jumlah_produk == 0:
            print("Tidak ada produk untuk dihapus!")
            return
        
        for i in range(this.jumlah_produk):
            if this.nama_produk[i] == nama:
                del this.id[i]
                del this.nama_produk[i]
                del this.kategori_produk[i]
                del this.harga_produk[i]
                this.jumlah_produk -= 1
                print("Produk berhasil dihapus!")
                return
        print("Produk tidak ditemukan!")
    
    def cari_produk(this, nama):
        if this.jumlah_produk == 0:
            print("Tidak ada produk untuk dicari!")
            return
        
        for i in range(this.jumlah_produk):
            if this.nama_produk[i] == nama:
                print(f"Produk ditemukan!\nID: {this.id[i]}, Kategori: {this.kategori_produk[i]}, Harga: {this.harga_produk[i]}")
                return
        print("Produk tidak ditemukan!")
