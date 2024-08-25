# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 15:49:52 2024

@author: Asus
"""

import math
a=float(input("so thuc a:"))
b=float(input("so thuc b:"))
s = (math.pow(a,1/2)) - (math.pow(b,1/2))/(a**(1/4) - b**(1/4)) - (math.pow(a,1/2)) + (a*b)**(1/4) / (a**(1/4) + b**(1/4))
print(s)