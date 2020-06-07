'''
A dictionary is a collection which is unordered, changeable and indexed.
In Python dictionaries are written with curly brackets, and they have keys and values.
'''
# example
mydict = {"ap":"amaravathi","telangana":"hyderabad",""}
print(mydict)
# access dictonary
print(mydict["ap"])
#loop through dictonary
for i,j in mydict.items():
    print(i,j)
# prints keys
for i in mydict.keys():
    print(i)
# prints values
for j in mydict.values():
    print(j)
    
# check key present in the dictonary
dict = {1:10,2:20,3:30,4:40,5:50}
if 9 in dict:
    print("present")
else:
    print("not present")
    
# Create a dictonary and its prints number and its squares in key-value pair
# example : {1:1,2:4,3:9,4:16,5:15}
num = int(input("enter the number : "))
dict = dict()
for i in range(1,num+1):
    dict[i] = i * i
print(dict)


# merge two dictonaries
dict1 = {"name":"sivaji"}
dict2 = {"surname":"marripudi"}
dict1.update(dict2)
print(dict1)

# delete a key in dictonarie
dict = {1:10,2:20,3:30,4:40,5:50}
del(dict[5])
print(dict)

# count the two dictonaries
# add two dictonaries and its prints to add values in common keys
from collections import Counter
dict1 = {1:10,2:20,3:30}
dict2 = {1:30,2:40,3:50}
d = Counter(dict1) + Counter(dict2)
print(d)

# print all unique values in a dictionary
dict = [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
list = []
for i in dict:
    for values in i.values():
        list.append(values)
print(set(list))

# soretd dictonary by using operator module
import operator
d = {"a":1,"b":2,"c":3,"d":4,"e":5}
res = sorted(dict,key = itemgetter(0),reverse = False)
print(res)

# how to check the dictonary is empty or not
dict = {4:"dgu"}
if not (dict):
    print("empty")
else:
    print(dict)
# In dictonarie to get the max and min value in dictonary
dict = {1:10,2:20,3:30,4:40,5:50,10:100,11:23,12:0}
list = []
for i in dict.values():
    list.append(i)
print(list)
a = max(list)
b = min(list)
print(a,b)


# How to remove duplicae values in dictonary
student_data = {'id1': 
   {'name': ['Sara'], 
    'class': ['V'], 
    'subject_integration': ['english, math, science']
   },
 'id2': 
  {'name': ['David'], 
    'class': ['V'], 
    'subject_integration': ['english, math, science']
   },
 'id3': 
    {'name': ['Sara'], 
    'class': ['V'], 
    'subject_integration': ['english, math, science']
   },
 'id4': 
   {'name': ['Surya'], 
    'class': ['V'], 
    'subject_integration': ['english, math, science']
   },
}

result = {}
for i,j in student_data.items():
    if j not in result.values():
        result[i] = j
print(result)

