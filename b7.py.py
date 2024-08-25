# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 14:58:33 2024

@author: Asus
"""

#in menu trực tiếp
print("============ MENU ============")
print("1. Hu tieu")
print("2. Chao long")
print("3. Banh canh")
print("4. Bún riêu")
print("5. Pho bo")
print("==============================")
#Nhập lựa chọn
lua_chon = input("Moi nhap lua chọn:")
print("===============================")
#xử lý lựa chọn
if lua_chon == '1':
    print("Ban da chon huu tieu")
elif lua_chon == '2':
    print("Ban da chon chao long")
elif lua_chon == '3':
    print("Ban da chon banh canh")
elif lua_chon == '4':
    print("Ban da chon bun rieu")
elif lua_chon == '5':
    print("Ban da chon pho bo")
else:
    print("lua chon khong hop le!")
    
