# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 14:40:34 2024

@author: Asus
"""
#nhập vào thời gian theo định dạng hh:mm:ss
time_input = input("Nhập vào giờ, phút và giây (định dạng hh:mm:ss): ")
hh, mm, ss = map(int, time_input.split(":"))
#kểm tra xem giờ, phút, giây có hợp lệ không
if 0<= hh < 24 and 0 <= mm < 60 and 0 <= ss < 60:
    #Đổi giờ, phút, giây ra giây
    total_seconds = hh * 3600 + mm * 60 + ss
       
    #in ra kết quả màn hình
    print("Tổng số giây",  total_seconds)
else:
    print(" giờ phút hoặc giây không hợp lệ. ")