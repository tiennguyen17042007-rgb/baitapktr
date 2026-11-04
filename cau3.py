
# Tao danh sach rong
ds = []

# Nhap danh sach
while True:
    n = int(input("Nhap so nguyen (0 de dung): "))
    if n == 0:
        break
    ds.append(n)

print("Danh sach:", ds)

# Tinh tong so duong chan
tong = 0
for x in ds:
    if x > 0 and x % 2 == 0:
        tong += x

print("Tong so duong chan:", tong)

# Dem so lan xuat hien cua k
k = int(input("Nhap k: "))
dem = 0

for x in ds:
    if x == k:
        dem += 1

print("So lan xuat hien cua", k, "la:", dem)
