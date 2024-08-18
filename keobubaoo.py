# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 16:36:46 2024

@author: Asus
"""
import random
choices = ["kéo", "búa", "bao"]
player = input("Nhập kết quả người chơi: ")
if player not in ["kéo", "búa", "bao"]:
    print("Kết quả không hợp lệ, nhập lại")
system = random.choice(choices)
print("Kết quả máy: ",system)
if player == system:
    print("Hòa!")
elif (player == "búa" and system == "kéo") or \
     (player == "kéo" and system == "bao") or \
     (player == "bao" and system == "búa"):
    print("Bạn thắng")
else:
    print("Bạn thua")



    