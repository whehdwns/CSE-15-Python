# -*- coding: utf-8 -*-
"""
Created on Thu Apr 12 11:58:05 2018

@author:whehdwns
"""

 #4. Implement Euclid's Algorithm for finding the greatest common divisor of two integers
def gcd(a, b):
    # Provide the correct implementation
    while b != 0:
        (a, b) = (b, a % b)
    return a
print (gcd(128, 60))
# Expected output: 4
