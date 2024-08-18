# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 14:10:24 2024

@author: Asus
"""
import math
#nhập nghiệm
a = float(input("nhập nghiệm a: "))
b = float(input("nhập nghiệm b:"))
c = float(input("nhập nghiệm c:"))
denta=b*b-4*a*c
if denta<0:
    print("phương trình vô nghiệm ")
elif denta==0:
    print("phương trình có nghiệm kép")
    print("x1=x2=", -b/2*a )
else:
    print("phương trình có hai nghiệm phân biệt ")
    x1 = (-b + math.sqrt(denta)) / (2 * a)
    x2 = (-b - math.sqrt(denta)) / (2 * a)
    print("x1 =", x1)
    print("x2 =", x2)
    
    
    
    
            
            
     
        
    

