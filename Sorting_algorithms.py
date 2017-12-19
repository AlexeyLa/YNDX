# -*- coding: utf-8 -*-
"""
Created on Tue Dec 19 11:00:38 2017

@author: a.lantsov
"""

import numpy as np
import scipy as sp
import time
#sys.setrecursionlimit(2000)

# best n - average n**2 - worst - n**2
def sortInsertion(x):
    for i in range(1,len(x)):
        j = i
        temp = x[j]
        while j > 0 and temp < x[j-1]:
            x[j] = x[j - 1]
            j = j - 1
        x[j] = temp    
    return x

def quicksort(arr):
    """ Quicksort a list

    :type arr: list
    :param arr: List to sort
    :returns: list -- Sorted list
    """
    if not arr:
        return []

    pivots = [x for x in arr if x == arr[0]]
    lesser = quicksort([x for x in arr if x < arr[0]])
    greater = quicksort([x for x in arr if x > arr[0]])

    return lesser + pivots + greater

array_a = list(np.random.rand(10000))
print("insertion sorting")
t = time.time()
sortInsertion(array_a)
print(time.time() - t)
print("done")
print("quicksort sorting")
t = time.time()
quicksort(array_a)
print(time.time() - t)
print("done")





