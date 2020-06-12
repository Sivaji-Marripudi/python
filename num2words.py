
# num2words module is used to convert number to words
# example:- input - 5,output - five

from num2words import num2words
dict = {}
list = []
for i in range(1,11):
    #dict[i] = num2words(i)
    list.append(num2words(i))
print(list)

from num2words import num2words
from collections import *
list = []
for i in range(1,11):
    j = num2words(i)
    list.append(j)
print(Counter(list))
