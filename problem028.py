#!/usr/bin/python3
#-*- coding: utf-8 -*-

import time
import math

start_time = time.time()

n = 1
corners = 1

for i in range(2, 1001, 2):
    for x in range(0, 4):    
        n += i
        corners += n

print(corners)
print("--- %s seconds ---" % (time.time() - start_time))      

