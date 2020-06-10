# list is a collection of heterogeneous data items
# list is a mutable i.e changble
# example of a list :-
list = ["siva",22,5.11,"india"]
print(list)
# access the list using index numbers
print(list[1]) # 22
print(list[0:len(list)+1]) # ["siva",22,5.11,"india"]
print(list[::-1]) # it prints reverse of a list
# loop through list
for i in list:
  print(i)
# add elements
# append,extend,insert
list = [1,2,3,4,5]
list.append(5)
print(list)
list.extend((6,7,8,9,10))
print(list)
list.insert(0,1)
print(list)
# del,remove,pop
# above methods are used to delete
li = ["hai","hello","ok","hmm"]
del li[2]
print(li)
li.remove("hmm")
print(li)
li.pop(0)
print(li)
li.clear()
print(li)
# sorted order i.e asec,desc
lis = [36,67,87,98,43,88,23,19,34,76]
lis.sort(reverse = True)
print(lis)
lis.sort(reverse = False)
print(lis)
print(sorted(lis))
# particular
l = ["hyd","bangalore","chennai","mumbai","ongole"]
a = l.index("ongole")
print(a)
#count
b = l.count("hyd")
print(b)
for i in l:
    print(i)
print(l[::-1])

# how to check if list is empty or not
list = []
if not list:
  print("empty")
else:
  print("not empty")
# remove duplicates from list
list = [1,1,2,2,2,3,4,2,5,5,6,4]
res = []
for i in list:
  if i not in res:
      res.append(i)
print(res)
########### or ##########
print(set(list))
######## or ########
from collections import Counter
res = []
A = Counter(list)
for i,j in A.items():
  res.append(i)
print(res)
####### or ########
# remove duplicates from orderwise
list = [1,1,1,1,2,2,2,3,3,3,4,4,5,6,6]
for i in list:
  if list.count(i)>1:
    list.remove(i)
print(list)

# multiplies all items in the list
list = [2,3,4,5,6,7]
res = 1
for i in list:
    res *= i
print(res)
# sum of all items in the list
# method 1
list = [2,3,4,53,56,76,45]
sum = 0
for i in list:
    sum += i
print(sum)
# Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings
list = ["abc","acd","xyz","1221","1341"]
res = []
for i in list:
    if len(i) > 1 and i[0] == i[-1]:
        res.append(i)
print(res)
print(len(res))
# check all elements are equal in list or not
list = [1,1,1,1,1,1]
first = list[0]
for i in list:
    if i != first:
        print("not equal")
        break
else:
    print("equal")
# returns true atleast one common member in two lists
list1 = [1,2,3,4,5,6,7,8,11,23,45]
list2 = [20,21,24,25,26,91]
common = []
for i in list1:
    for j in list2:
        if i == j:
            common.append(i)
print(common)
if len(common) > 0:
    print(True)
else:
    print(False)
# longer word in list
def longer(list,n):
    res = []
    for i in list:
        if len(i) > n:
            res.append(i)
    print(res)
    print(len(res))
longer(["sivaji","ongole","hyderabad","bangalore","python","django"],5)
# how to add two lists by the position of index numbers
list1 = [10,9,8]
list2 = [1,2,3]
res = [i+j for i,j in zip(list1,list2)]
print(res)
# Another method
res1 = []
for i in range(len(list1)):
  res1.append(list1[i] + list2[i])
print(res1)
# find smallest and largest number in list
list = [88,87,95,48,63,100,34,23,54,1,2,3,4,5,6,7,8,9]
a = sorted(list)
print(a[1]) # second smallest number
print(a[-2]) # second largest number
# converts nested list to list
list = [[1,2,3],[4,5,6],[7,8,9]]
res = []
for i in list:
    res.extend(i)
print(res)
# find numbers above 40 in list
list = [10,20,30,40,50,60,70,80,90,100]
res = []
for i in range(40,100+1):
    if i in list:
        res.append(i)
print(res)
print(len(res))
# converts list to string without using methods
list = [1,2,3]
res = ""
for i in list:
    i = str(i)
    res += i
print(res)
# find common numbers in two lists
list1 = [1,2,3,4,5,6,7,8,9,10]
list2 = [11,12,13,4,5,16,17]
res1 = []
res2 = []
if list1 in list2:
    res1.append(list1)
elif list2 in list1:
    res2.append(list2)
else:
    pass
print(res1)
print(res2)
