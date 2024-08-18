# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 15:45:49 2024

@author: Asus
"""
#nhập độ dài 3 cạnh
a = float(input("nhập độ dài cạnh thứ nhất: "))
b = float(input("nhập độ dài cạnh thứ hai: "))
c = float(input("nhập độ dài cạnh thứ ba: "))
if a*a==b*b+c*c or b*b==a*a+c*c or c*c==b*b+a*a:
   print("đây là tam giác vuông")
elif a==b or b==c:
    print("đây là tam giác đều")
if a==b and b==c and c==a:
    print("đây là tam giác vuông cân ")
elif a*a>b*b+c*c or b*b>a*a+c*c or c*c>b*b+a*a:
    print("đây là tam giác tù")
else:
    print("đây là tam giác thường")
    
    
