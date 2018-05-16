# -*- coding: utf-8 -*-
"""
Created on Thu Apr 12 11:53:54 2018

@author: Dongjun
"""

def cartesian_product(X, Y):  # This is trivial
    ans = []
    for x in X:
        for y in Y:
            ans.append((x, y))
    return ans


X = ['a', 'e']
Y = [1, 3, 7, 9]

print (cartesian_product(X, Y))
