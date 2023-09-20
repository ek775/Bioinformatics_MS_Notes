# -*- coding: utf-8 -*-
"""
Created on Mon Sep 18 14:07:19 2023

@author: ninja
"""
seq = "ABCDEFGHIJKLMNOPQRSTUVWXYZNOWIKNOWMYABCSWONTYOUSINGALONGWITHME"
count = {}
for i in seq:
    if i in count:
        count[i]+=1
    else:
        count[i]=1
        
print(count)   