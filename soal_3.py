# input jumlah barang
jumlah_barang = int(input("masukan jumlah barang:"))
# inisialisasi total harga
total_harga = 0
#input harga per barang
for i in range (1,jumlah_barang+1):
    harga_barang = float(input(f"masukan harga barang ke-{i}:"))
    total_harga +=harga_barang
#total harga belanjaan 
print(f"total belanjaan : Rp.{total_harga:2f}") 