'''
A dictionary is a collection which is unordered, changeable and indexed.
In Python dictionaries are written with curly brackets, and they have keys and values.
'''
# example
mydict = {"ap":"amaravathi","telangana":"hyderabad",""}
print(mydict)
# access dictonary
print(mydict["name"])
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
