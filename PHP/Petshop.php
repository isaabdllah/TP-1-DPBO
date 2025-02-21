<?php

class Petshop
{
    private $id;
    private $namaProduk;
    private $kategoriProduk;
    private $hargaProduk;
    private $fotoProduk;

    public function __construct($id, $namaProduk, $kategoriProduk, $hargaProduk, $fotoProduk)
    {
        $this->id = $id;
        $this->namaProduk = $namaProduk;
        $this->kategoriProduk = $kategoriProduk;
        $this->hargaProduk = $hargaProduk;
        $this->fotoProduk = $fotoProduk;
    }

    public function setId($id)
    {
        $this->id = $id;
    }

    public function getId()
    {
        return $this->id;
    }

    public function setNamaProduk($namaProduk)
    {
        $this->namaProduk = $namaProduk;
    }

    public function getNamaProduk()
    {
        return $this->namaProduk;
    }

    public function setKategoriProduk($kategoriProduk)
    {
        $this->kategoriProduk = $kategoriProduk;
    }

    public function getKategoriProduk()
    {
        return $this->kategoriProduk;
    }

    public function setHargaProduk($hargaProduk)
    {
        $this->hargaProduk = $hargaProduk;
    }

    public function getHargaProduk()
    {
        return $this->hargaProduk;
    }

    public function setFotoProduk($fotoProduk)
    {
        $this->fotoProduk = $fotoProduk;
    }

    public function getFotoProduk()
    {
        return $this->fotoProduk;
    }
}