
s = input("Nhap chuoi s: ")

# Dem so ky tu chu hoa
dem = 0
for i in s:
    if i.isupper():
        dem += 1

print("So ky tu chu hoa:", dem)

# Kiem tra chuoi doi xung
if s == s[::-1]:
    print("Chuoi doi xung")
else:
    print("Chuoi khong doi xung")

# Tinh tong cac chu so
tong = 0
for i in s:
    if i.isdigit():
        tong += int(i)

print("Tong cac chu so:", tong)
