# sum all the items in list
li = [1,1,1,1,1,2,2,2,3]
sum = 0
for i in li:
    sum += i
print(sum)

# multiplies all the itmes in list
li = [5,6,7,3,5,6,7]
mul = 1
for i in li:
    mul *= i
print(mul)

# to get the largest number in list
li = [4,5,6,2,3,24,4,11]
lar = li[0]
for i in li:
    if i > lar:
        lar = i
    else:
        pass
print(lar)
# another method to get largest item in list
print(max(li)) # 'max' is a built_in method in list

#to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings
#Sample List : ['abc', 'xyz', 'aba', '1221'],Expected Result : 2
li = ['abc','xyz','aba','1221']
for i in li:
    if (len(i) >= 2) and (i[0] == i[-1]):
        print(i)
    else:
        pass

#Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples.
#Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)],Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]

# remove duplicates in list
li = [4,5,6,3,4,5,7,23,3,4,1,1,1,7,6,5,8,9]
res = []
for i in li:
    if i not in res:
        res.append(i)
print(res)
############################### ANOTHER METHOD 
from collections import Counter
new = []
a = Counter(li)
for i,j in a.items():
    new.append(i)
print(new)
########## ANOTHER METHOD 
print(set(li))

# check list is empty or not
li = []
if not li:
    print('list is empty')
else:
    print('list is not empty')

#  Write a Python function that takes two lists and returns True if they have at least one common member.
def lists(a,b):
    for i in a:
        for j in b:
            if i == j:
                return 'found'
    else:
        return 'not found'
res = lists([11,12,14,34,22,65,77],[99,56,87,33,99,10,3,6,77])
print(res)

# Write a Python program to find the list of words that are longer than n from a given list of words.
def check(a,n):
    res = []
    for i in a:
        if len(i) > n:
            res.append(i)
    print(res)
check(['hyderabad','bangalore','chennai','kolkata','ongole','mumbai','pune','noida'],4)

# removing even numbers in list
li = [1,2,3,4,5,6,7,8,9,11,13]
res = [i for i in li if i % 2 != 0]
print(res)

# removing odd numbers in list
li = [22,3,4,55,4,3,66,77,88]
res = [i for i in li if i % 2 == 0]
print(res)

#  Write a Python program to generate and print a list of first and last 5 elements where the values are square of numbers between 1 and 30 (both included).
res = [i**2 for i in range(1,31)]
new_res = []
new_res.extend(res[0:5])
new_res.extend(res[-5:])
print(new_res)

# Write a Python program access the index of a list.
list = ["ap","tn","ka","mh","py","jk","go","ts"]
for i,j in enumerate(list):
    print(i,j)

# Write a Python program to convert a list of characters into a string.
li = ['hai','how','are','you!']
print(' '.join(li))

# get index of item in a list
print(li.index('hai'))
