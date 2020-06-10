# string is a group of characters 
# example
string = "sivaji"
print(string)
# multiline string
str = ''' Python is a popular programming language. It was created by Guido van Rossum, and released in 1991.
It is used for:
web development (server-side),
software development,
mathematics,
system scripting. 
'''
print(str)
# input :- httpwwwsivajicom output:-http://www.sivaji.com
a = "httpwwwsivajicom"
b = a.replace("p","p://")
b = b.replace("s",".s")
b = b.replace("c",".c")
print(b)
# count words
para = "jhgksdyjdiod jfwlfwj jilfwkfj figwiofyek fiegfeoil fih3ilb diofheil hoilihoi kfhefoib lfhoil "
print(para.count(" ") + 1)
###### or ####
from collections import Counter
para = "jhgksdyjdiod jfwlfwj jilfwkfj figwiofyek fiegfeoil fih3ilb diofheil hoilihoi kfhefoib lfhoil ".split()
words = Counter(para)
print(words)
# find number of palindrome words in text
palin = []
for i in words:
    if(i == i[::-1]):
        palin.append(i)
print(palin)
print(len(palin))
