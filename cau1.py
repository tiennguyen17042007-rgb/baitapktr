# Chuong trinh chinh

# Nhap n va kiem tra dieu kien
n = int(input("Nhap n: "))

while n < 1 or n > 1500:
    print("Nhap lai n trong khoang [1, 1500]!")
    n = int(input("Nhap n: "))

# Dem so chu so le
dem = 0
tam = n

while tam > 0:
    chuso = tam % 10

    if chuso % 2 != 0:
        dem += 1

    tam //= 10

print("So chu so le:", dem)

# Tinh tong S
S = 0

for i in range(1, n + 1):
    S += 1 / (2 * i)

print("Tong S =", S)