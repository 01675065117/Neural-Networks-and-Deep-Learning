# -*- coding: utf-8 -*-
"""
Created on Fri Jun 17 15:00:43 2022

@author: Tran Minh Khoa
"""

import numpy as np
import time
a = np.random.rand(1000000)
b = np.random.rand(1000000)

tic = time.time()
c = np.dot(a,b)
toc = time.time()
print(c)
print("Vectorized: ", str(1000*(toc-tic))," ms")

c = 0
tic = time.time()
for i in range(1000000):
    c += a[i]*b[i]
toc = time.time()

print(c)
print("For Loop: ", str(1000*(toc-tic))," ms")
