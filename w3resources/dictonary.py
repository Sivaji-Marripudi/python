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

