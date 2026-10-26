# #input
# nilai = int (input("masukan nilai:"))
# # proses
# if nilai >=80 and nilai <=100:
#     print("anda mendapatkan nilai A")
# elif nilai >=70 and nilai <=80:
#     print("anda mendapatkan nilai B")
# elif nilai >=50 and nilai <=70:
#     print("anda mendapatkan nilai C")
# elif nilai >=30 and nilai <=50:
#     print("anda mendapatkam nilai D")
# elif nilai >=0 and nilai <=20:
#     print("anda mendapatkan nilai E")
# else:
#     print("data tidak valid")




print("=====latihan=====")
#input
nama_barang = input("masukan nama barang:")
harga_barang = int(input("masukan harga barang:"))
#proses
if nama_barang.lower() =="kulkas":
    diskon = 0.10 *harga_barang
elif nama_barang.lower()=="TV":
    diskon = 0.5 *harga_barang
elif nama_barang.lower() =="radio":
    diskon = 0
else:
    print ("nama barang tidak tersedia")
    diskon = 0

jumlah_bayar = harga_barang - diskon

#output
print("================")
print("nama_barang :",nama_barang)
print("harga_barang:",harga_barang)
print("diskon      :",diskon)
print("jumlah_bayar:",jumlah_bayar)
print("================")
    