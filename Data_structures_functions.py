# -*- coding: utf-8 -*-
"""
Created on Tue Dec 19 11:44:15 2017

@author: a.lantsov
"""

from functools import reduce

# lambda

f = lambda x: 2*x
print(f(10))

# map

list_my = [1,2,3,4,5]
squaredList = map(f, list_my)
print(list(squaredList))

# filter

list_my = [1,2,3,4,5]
newList = filter(lambda x: x % 2==0, list_my)
print(list(newList))

# reduce

list_my = [1,2,3,4,5]
s = reduce(lambda x,y: x * y, list_my)
print(s)

# LOOKUP SPEED

# dictionary to use as the lookup dictionary
lookupdict = {
     1: "val1",
     2: "val2",
    27: "val3",
    35: "val4",
    59: "val5" }

# some test data

t = time.time()
arr = np.random.choice(list(lookupdict.keys()),1000000)
res = [lookupdict[k] for k in arr]
print(time.time() - t)