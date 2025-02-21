import java.util.ArrayList;
import java.util.Scanner;

public class Main {
    private static ArrayList<Petshop> daftarProduk = new ArrayList<>();
    private static Scanner input = new Scanner(System.in);

    public static void main(String[] args) {
        int menu;

        do {
            System.out.println("\nMenu:");
            System.out.println("1. Tampilkan Data");
            System.out.println("2. Tambah Data");
            System.out.println("3. Edit Data");
            System.out.println("4. Hapus Data");
            System.out.println("5. Cari Data");
            System.out.println("6. Keluar");
            System.out.print("Pilih Menu: ");
            menu = input.nextInt();
            input.nextLine(); // Flush buffer

            switch (menu) {
                case 1:
                    tampilkanProduk();
                    break;
                case 2:
                    tambahProduk();
                    break;
                case 3:
                    editProduk();
                    break;
                case 4:
                    hapusProduk();
                    break;
                case 5:
                    cariProduk();
                    break;
                case 6:
                    System.out.println("Terima kasih sudah menggunakan program ini!");
                    break;
                default:
                    System.out.println("Pilihan tidak valid! Silakan pilih menu yang tersedia.");
            }
        } while (menu != 6);
    }

    // Menampilkan semua produk
    private static void tampilkanProduk() {
        if (daftarProduk.isEmpty()) {
            System.out.println("Data kosong, tidak ada produk di PetShop!");
            return;
        }

        System.out.println("\nDaftar Produk di PetShop:");
        for (Petshop p : daftarProduk) {
            System.out.println("ID: " + p.getId() + ", Nama: " + p.getNama() + ", Kategori: " + p.getKategori() + ", Harga: " + p.getHarga());
        }
    }

    // Menambahkan produk baru dengan ID unik
    private static void tambahProduk() {
        System.out.print("Masukkan ID: ");
        int id = input.nextInt();
        input.nextLine(); // Flush buffer

        // Cek apakah ID sudah ada
        for (Petshop p : daftarProduk) {
            if (p.getId() == id) {
                System.out.println("Produk dengan ID " + id + " sudah ada! Gagal menambahkan produk.");
                return;
            }
        }

        System.out.print("Masukkan Nama Produk: ");
        String nama = input.nextLine();

        System.out.print("Masukkan Kategori Produk: ");
        String kategori = input.nextLine();

        System.out.print("Masukkan Harga Produk: ");
        int harga = input.nextInt();

        daftarProduk.add(new Petshop(id, nama, kategori, harga));
        System.out.println("Produk berhasil ditambahkan!");
    }

    // Mengedit produk berdasarkan nama
    private static void editProduk() {
        if (daftarProduk.isEmpty()) {
            System.out.println("Tidak ada produk untuk diedit!");
            return;
        }

        System.out.print("Masukkan nama produk yang ingin diedit: ");
        String nama = input.nextLine();

        for (Petshop p : daftarProduk) {
            if (p.getNama().equalsIgnoreCase(nama)) {
                System.out.print("Masukkan ID baru: ");
                int idBaru = input.nextInt();
                input.nextLine();

                System.out.print("Masukkan Nama Produk baru: ");
                String namaBaru = input.nextLine();

                System.out.print("Masukkan Kategori Produk baru: ");
                String kategoriBaru = input.nextLine();

                System.out.print("Masukkan Harga Produk baru: ");
                int hargaBaru = input.nextInt();

                p.setId(idBaru);
                p.setNama(namaBaru);
                p.setKategori(kategoriBaru);
                p.setHarga(hargaBaru);

                System.out.println("Produk berhasil diperbarui!");
                return;
            }
        }
        System.out.println("Produk tidak ditemukan!");
    }

    // Menghapus produk berdasarkan nama
    private static void hapusProduk() {
        if (daftarProduk.isEmpty()) {
            System.out.println("Tidak ada produk untuk dihapus!");
            return;
        }

        System.out.print("Masukkan nama produk yang ingin dihapus: ");
        String nama = input.nextLine();

        for (int i = 0; i < daftarProduk.size(); i++) {
            if (daftarProduk.get(i).getNama().equalsIgnoreCase(nama)) {
                daftarProduk.remove(i);
                System.out.println("Produk berhasil dihapus!");
                return;
            }
        }
        System.out.println("Produk tidak ditemukan!");
    }

    // Mencari produk berdasarkan nama
    private static void cariProduk() {
        if (daftarProduk.isEmpty()) {
            System.out.println("Tidak ada produk untuk dicari!");
            return;
        }

        System.out.print("Masukkan nama produk yang dicari: ");
        String nama = input.nextLine();

        for (Petshop p : daftarProduk) {
            if (p.getNama().equalsIgnoreCase(nama)) {
                System.out.println("Produk ditemukan!\nID: " + p.getId() + ", Kategori: " + p.getKategori() + ", Harga: " + p.getHarga());
                return;
            }
        }
        System.out.println("Produk tidak ditemukan!");
    }
}
