# -*- coding: utf-8 -*-
"""
Created on Fri Jun 17 16:45:07 2022

@author: Tran Minh Khoa
"""

import numpy as np
A = np.array([[56.0, 0.0, 4.4, 68.0],[1.2, 104.0, 52.0, 8.0], [1.8, 135.0, 99.0, 0.9]])
cal = A.sum(axis=0)
percentage = 100*A/cal