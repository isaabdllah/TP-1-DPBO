<?php
require_once 'Petshop.php';
session_start();

// Pastikan folder uploads ada
if (!is_dir('uploads')) {
    mkdir('uploads', 0777, true);
}

// Inisialisasi data jika belum ada
if (!isset($_SESSION['produk'])) {
    $_SESSION['produk'] = [];
}

// Handle Form
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    if (isset($_POST['add'])) {
        $id = $_POST['idProduk']; // ID dari input form
        $nama = $_POST['namaProduk'];
        $kategori = $_POST['kategoriProduk'];
        $harga = $_POST['hargaProduk'];

        // Cek apakah ID sudah ada
        if (isset($_SESSION['produk'][$id])) {
            echo "<script>alert('ID sudah digunakan! Pilih ID lain.');</script>";
        } else {
            // Simpan foto
            $fotoNama = $_FILES['fotoProduk']['name'];
            $fotoTmp = $_FILES['fotoProduk']['tmp_name'];
            $fotoPath = 'uploads/' . $fotoNama;
            move_uploaded_file($fotoTmp, $fotoPath);

            // Tambahkan produk ke session
            $_SESSION['produk'][$id] = new Petshop($id, $nama, $kategori, $harga, $fotoPath);
        }
    }
    
    if (isset($_POST['delete'])) {
        $id = $_POST['id'];
        if (isset($_SESSION['produk'][$id])) {
            unlink($_SESSION['produk'][$id]->getFotoProduk()); // Hapus gambar dari folder
            unset($_SESSION['produk'][$id]); // Hapus dari session
        }
    }
    header('Location: '.$_SERVER['PHP_SELF']);
    exit;
}
?>
<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Petshop CRUD</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            text-align: center;
            background: #f4f4f4;
            margin: 0;
            padding: 20px;
        }
        .container {
            max-width: 800px;
            margin: 0 auto;
            background: white;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }
        h2 {
            color: #333;
        }
        form {
            display: flex;
            flex-direction: column;
            align-items: center;
            gap: 10px;
        }
        input, button {
            width: 100%;
            padding: 10px;
            margin: 5px 0;
            border: 1px solid #ccc;
            border-radius: 5px;
            font-size: 16px;
        }
        button {
            background: #007bff;
            color: white;
            border: none;
            cursor: pointer;
            transition: 0.3s;
        }
        button:hover {
            background: #0056b3;
        }
        table {
            width: 100%;
            margin-top: 20px;
            border-collapse: collapse;
        }
        th, td {
            padding: 12px;
            text-align: left;
            border: 1px solid #ddd;
        }
        th {
            background: #007bff;
            color: white;
        }
        img {
            width: 80px;
            height: auto;
            border-radius: 5px;
        }
        .delete-btn {
            background: #dc3545;
        }
        .delete-btn:hover {
            background: #b02a37;
        }
    </style>
</head>
<body>
    <div class="container">
        <h2>Tambah Produk</h2>
        <form method="POST" enctype="multipart/form-data">
            <input type="text" name="idProduk" placeholder="ID Produk" required>
            <input type="text" name="namaProduk" placeholder="Nama Produk" required>
            <input type="text" name="kategoriProduk" placeholder="Kategori" required>
            <input type="number" name="hargaProduk" placeholder="Harga" required>
            <input type="file" name="fotoProduk" accept="image/*" required>
            <button type="submit" name="add">Tambah Produk</button>
        </form>
        
        <h2>Daftar Produk</h2>
        <table>
            <tr>
                <th>ID</th>
                <th>Nama Produk</th>
                <th>Kategori</th>
                <th>Harga</th>
                <th>Foto</th>
                <th>Aksi</th>
            </tr>
            <?php foreach ($_SESSION['produk'] as $produk) { ?>
            <tr>
                <td><?= htmlspecialchars($produk->getId()); ?></td>
                <td><?= htmlspecialchars($produk->getNamaProduk()); ?></td>
                <td><?= htmlspecialchars($produk->getKategoriProduk()); ?></td>
                <td>Rp <?= number_format($produk->getHargaProduk(), 0, ',', '.'); ?></td>
                <td><img src="<?= htmlspecialchars($produk->getFotoProduk()); ?>" alt="Foto Produk"></td>
                <td>
                    <form method="POST">
                        <input type="hidden" name="id" value="<?= htmlspecialchars($produk->getId()); ?>">
                        <button type="submit" name="delete" class="delete-btn">Hapus</button>
                    </form>
                </td>
            </tr>
            <?php } ?>
        </table>
    </div>
</body>
</html>