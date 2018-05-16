# -*- coding: utf-8 -*-
"""
Created on Thu Apr 12 11:56:22 2018

@author: Dongjun
"""
#3. Given two sorted lists, it is possible to merge them into one sorted lists
#in an efficient way. Design and implement a divide and conquer algorithm
#to merge two sorted lists.
def merge(list1, list2):
    # Provide your code here
    size = len(list1) + len(list2)
    list3 = [None] * size

    for i in range(0, len(list1)):
        list3[i] = list1[i]

    for j in range(0, len(list2)):
        list3[len(list1) + j] = list2[j]
    k = 0

    while k < len(list3):
        largest = list3[0]
        loc = 0

        for m in range(0, size):
            if(list3[m] > largest):
                largest = list3[m]
                loc = m
        temp = list3[size - 1]
        list3[size - 1] = largest
        list3[loc] = temp
        size = size - 1
        k = k + 1
    return list3

print ("merge([1, 3, 5, 7], [2, 4, 6, 8]):\t", merge([1, 3, 5, 7], [2, 4, 6, 8]))
# should return [1, 2, 3, 4, 5, 6, 7, 8]
