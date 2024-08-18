# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 13:48:20 2024

@author: Asus
"""

a=float(input("a:"))
b=float(input("b:"))
if a ==0:
    if b==0:
        print("Phương trình vô số nghiệm")
    else: 
        print("Phương trình có nghiệm")
else:
     x=-b/a
     print("Phương trình cò một nghiệm x",x)
        
        