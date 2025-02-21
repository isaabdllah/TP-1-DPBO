#include "Petshop.cpp"

int main()
{
    PetShop petshop;
    int menu;

    while (menu != 6)
    {
        cout << "\nMenu:\n";
        cout << "1. Tampilkan Data\n";
        cout << "2. Tambah Data\n";
        cout << "3. Edit Data\n";
        cout << "4. Hapus Data\n";
        cout << "5. Cari Data\n";
        cout << "6. Keluar\n";
        cout << "Pilih Menu: ";
        cin >> menu;

        switch (menu)
        {
        case 1:
            petshop.tampilkanProduk();
            break;
        case 2:
            petshop.tambahProduk();
            break;
        case 3:
            petshop.editProduk();
            break;
        case 4:
            petshop.hapusProduk();
            break;
        case 5:
            petshop.cariProduk();
            break;
        case 6:
            cout << "Terima kasih sudah menggunakan program ini!\n";
            break;
        default:
            cout << "Pilihan tidak valid! Silakan pilih menu yang tersedia.\n";
        }
    }

    return 0;
}
