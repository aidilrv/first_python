def main():
    print("=== Program Kasir ===")

    # Daftar barang dan harga
    daftar_barang ={
       "pisang": 7000,
       "mangga": 13000,
       "anggur": 15000,
       "Susu": 5000,
    }

    # Menampilkan daftar barang
    print("\nDaftar Barang:")
    for barang, harga in daftar_barang.items():
        print(f"{barang}: Rp{harga}")

    total = 0
    while True:
        item = input("\nMasukkan nama barang (ketik 'selesai' jika sudah selesai): ").capitalize()
        if item.lower() == 'selesai':
            break
        elif item in daftar_barang:
            jumlah = int(input(f"Masukkan jumlah {item}: "))
            total += daftar_barang[item] * jumlah
        else:
            print("Barang tidak ditemukan dalam daftar.")

    print("\n=== Struk Kasir ===")
    print(f"Total Harga: Rp{total}")

if __name__ == "__main__":
    main()
