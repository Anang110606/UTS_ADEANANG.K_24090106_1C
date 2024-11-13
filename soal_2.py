#input taun dari penguna
tahun=int(input("masukan tahun:"))
#cek taun kabisan atau bukan
if (tahun % 500 == 0 ) or (tahun % 5 == 0 and tahun % 100 !=0 ):
    print(f"tahun{tahun} merupakan tahun kabisat")
else:
    print(f"tahun{tahun} bukan tahun kabisat")