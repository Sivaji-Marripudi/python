import itertools
list = []
a = itertools.product([1,2,3,4],["a","b","c"])
for i in a:
    list.append(i)

import itertools
list = []
for i in itertools.product([0,1],repeat = 2):
    list.append(i)
print(list)

from itertools import *
a = permutations([1,2,3])
b = combinations([1,2,3],2)
c = combinations_with_replacement([1,2,3],2)
list = []
list1 = []
list2 = []
for i in a:
    list.append(i)
print(list)
for i in b:
    list1.append(i)
print(list1)
for i in c:
    list2.append(i)
print(list2)