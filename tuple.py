'''
Tuple is a collection of heterogeneous data items
tuple is immutable i.e not changble
'''
# example
tuple = (1,2,"hai",5.1)
print(tuple)
# access the tuple using index
print(tuple[1]) # 2
# loop through tuple
for i in tuple:
  print(i)
# coverts tuple to list
print(list(tuple))

tuple = (1,2,3,4,5,5,5,5,5,5)
tuple2 = ("A","B","C","D","E","a","b","c","d")
tuple1 = (6,7,8,9,10)
print(tuple.count(5))
print(tuple.index(5))
print(max(tuple))
print(min(tuple))
print(sum(tuple))
print(ascii(tuple2))
print(list(zip(tuple)))
for i in tuple:
    if i == 5:
        break
    print(i)
for j in tuple1:
    if i == 7:
        continue
    print(j)
# convert tuple to string
tuple = ("sivaji","marripudi")
tuple = " ".join(tuple)
print(tuple)

from collections import *
tuple = (1,2,3,4,5,6,7,8,1,2,1,2,3)
a = Counter(tuple)
rep = []
for i,j in a.items():
    if j > 1:
        rep.append(i)
print(rep)
# how to get index number in tuple
tuple = (1,2,3)
print(tuple.index(2))
# convert tuple to dictonary
tuple = ((1,"sivaji"),(2,"ram"),(3,"raj"),(4,"venki"))
print(dict((x,y) for x,y in tuple))

tuple = [('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')]
print(sorted(tuple,reverse = True))

# covert string format
tuple = (1,2,3)
str = str(tuple)
print("this is an tuple",str)

tuple = [(1,2,3),(4,5,6),(7,8,9)]
res = []
for i in tuple:
    a = list(i)
    a.pop(-1)
    a.append(100)
    print(a)
    res.append(a)
print(res)