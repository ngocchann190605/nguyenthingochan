# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 16:06:10 2024

@author: Asus
"""
#nhap chuoi ban dau
chuoi = "Đại học Quốc gia, Khu phố 6, P. Linh Trung, Q. Thủ Đức, Tp. HCM"
# Tách chuỗi
chuoia = [s.strip() for s in chuoi.split(",")]

#danh sach 1
danhsach1 = chuoia

#danhsach 2
chuoi= chuoi.replace("P. ","").replace("Q. ","").replace("Tp. ","")
chuoi = [s.strip() for s in chuoi.split(",")]
#in danh sach
print("Danh sách 1:")
for item in danhsach1:
    print(item)
print("Danh sách 2:")
for item in chuoi:
    print(item)