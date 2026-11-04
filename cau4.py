
# Tao tu dien rong
sach = {}

# Nhap so luong sach
n = int(input("Nhap so luong sach: "))

# Nhap thong tin sach
for i in range(n):
    print("\nNhap sach thu", i + 1)

    ma = input("Nhap ma sach: ")
    ten = input("Nhap ten sach: ")
    tacgia = input("Nhap ten tac gia: ")
    nxb = input("Nhap nha xuat ban: ")
    nam = int(input("Nhap nam xuat ban: "))

    sach[ma] = [ten, tacgia, nxb, nam]

# In danh sach sach
print("\nDANH SACH SACH")
for ma in sach:
    print("Ma sach:", ma)
    print("Ten sach:", sach[ma][0])
    print("Tac gia:", sach[ma][1])
    print("Nha xuat ban:", sach[ma][2])
    print("Nam xuat ban:", sach[ma][3])

# Nhap ma sach can xoa
ma_tim = input("\nNhap ma sach can xoa: ")

# Tim va xoa sach
if ma_tim in sach:
    del sach[ma_tim]
    print("Da xoa sach!")
else:
    print("Khong tim thay cuon sach can xoa.")

# In danh sach sau khi xoa
print("\nDANH SACH SAU KHI XOA")
for ma in sach:
    print(ma, sach[ma])
