# sort dictonary by value
import operator
mydict = {'ap':'amaravathi','tn':'chen','kn':'bnglr','ke':'thriva','goa':'panaji','ts':'hyd'}
print(dict(sorted(mydict.items(),key = operator.itemgetter(1))))

# Sorted dict by values in DESC
from collections import Counter
a = Counter(mydict)
print(a)

# add key to a dict
mydict = {0:10,1:20,2:30}
mydict.update({3:40})
print(mydict)

#Write a Python script to concatenate following dictionaries to create a new one.
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
dic = {}
for i in (dic1,dic2,dic3):
    dic.update(i)
print(dic)

# Write a Python script to check whether a given key already exists in a dictionary.
mydict = {'ap':'amaravathi','tn':'chen','kn':'bnglr','ke':'thriva','goa':'panaji','ts':'hyd'}
if 'ap' in mydict.keys():
    print('already exists')
else:
    print('not exists')

# Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x).
dic = {n:n**2 for n in range(1,5+1)}
print(dic)
######### Another method
dict = {}
for i in range(1,11):
    dict[i] = i * i
print(dict)

#  Write a Python program to sum all the items in a dictionary
dic =  {1:3,2:5,3:50,4:58,5:44,6:44,7:98,8:34}
sum = 0
for i,j in dic.items():
    sum += j
print(sum)

# Write a Python program to remove a key from a dictionary
dic =  {1:3,2:5,3:50,4:58,5:44,6:44,7:98,8:34}
if 7 in dic.keys():
    del dic[7]
print(dic)

# Write a Python program to get the maximum and minimum value in a dictionary
dic = {1:3,2:5,3:50,4:58,5:44,6:44,7:98,8:34}
li = []
for i,j in dic.items():
    li.append(j)
print(min(li))
print(max(li))

#  Write a Python program to check a dictionary is empty or not.
dic = {}
if not dic:
    print('empty')
else:
    print('not empty')

# check whether it is a dict or not,if it is a dict prints True otherwise  False
dic = {1:'ap',2:'ts'}
print(isinstance(dic,dict))
# map two lists into a dictonary
l1 = ['ap','ts','tn','kn','ke','go','mh']
l2 = ['am','hyd','che','bnglr','thir','panaji','mumb']
res = []
for i in zip(l1,l2):
    res.append(i)
print(dict(res))
############# ANOTHER METHOD
a = dict(zip(l1,l2))
print(a)

# remove duplicate values in dict
dic = {1:10,2:20,3:30,4:10,5:50,6:60,10:10}
res = {}
for i,j in dic.items():
    if j not in res.values():
        res[i] = j
print(res)

# Write a Python program to print all unique values in a dictionary. 
mydict =  [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"},{"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
li = []
for i in mydict:
    for a in i.values():
        li.append(a)
print(set(li))

# Write a Python program to create and display all combinations of letters, selecting each letter from a different key in a dictionary.
# Sample data : {'1':['a','b'], '2':['c','d']},Expected Output: ac ad bc bd
mydict = {'1':['a','b'], '2':['c','d']}
res = []
res1 = []
for i in mydict.values():
    res.extend(i)
for i in res[0:len(res)//2]:
    for j in res[len(res)//2:]:
        print(i + j)

# Write a Python program to combine values in python list of dictionaries. 
# Sample data: [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]
# Expected Output: Counter({'item1': 1150, 'item2': 300})'''
'''
n = int(input('enter the number : '))
dict = {}
for i in range(n):
    name,*marks = input('enter the : ').split()
    new_marks = list(map(float,marks))
    dict[name] = new_marks
name = input('do you want which student avg marks ? ')
if name in dict.keys():
    print('avg is : ')
    a = dict[name]
    avg = sum(a)//len(a)
    print(avg)
else:
    print('plz enter valid student)


# find a avg marks of a particular student 
n = int(input('enter the n '))
marks = []
details = {}
for i in range(n):
    stu_name,*stu_marks = input('enter the students with_marks also : ').split()
    details.setdefault(stu_name,stu_marks)
name = input('do you want which student avg marks : ')
if name in details.keys():
    for i in details.values():
        for j in i:
            k = float(j)
            marks.append(k)
            avg = sum(marks)/len(marks)
    print(avg)
if avg >= 80 and avg <= 99:
    print(name,'has A grade ')
elif avg >= 60 and avg <= 79:
    print(name,'has B grade' )
else:
    print(name,'has less score')
