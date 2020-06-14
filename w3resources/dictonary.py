# sort dictonary by value
import operator
mydict = {'ap':'amaravathi','tn':'chen','kn':'bnglr','ke':'thriva','goa':'panaji','ts':'hyd'}
print(dict(sorted(mydict.items(),key = operator.itemgetter(1))))

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
    