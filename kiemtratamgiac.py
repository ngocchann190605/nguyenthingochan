# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 15:08:58 2024

@author: Asus
"""

#nhập dộ dài 3 cạnh
a = float(input("nhập độ dài cạnh thứ nhất: "))
b = float(input("nhập độ dài cạnh thứ hai: "))
c = float(input("nhập độ dài cạnh thứ ba: "))

#kiểm tra ba cạnh có tạo hình một tam giác hay không
if a==0 or b==0 or c==0:
    print("một cạnh của một tam giác vuông ")
if a+b+c>c and b+c>b and b+c>a:
    print("a,b,c là 3 cạnh của một tam giác ")
else:
     print("không xát định ")
     