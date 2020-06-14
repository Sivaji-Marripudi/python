# count words in text
text = 'hai,good morning!'
words = text.count(" ") + 1
print(words)
#### ANOTHER METHOD
from collections import Counter
words = Counter(text.split())
print(words)

# Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string. If the string length is less than 2, return instead of the empty string
text = input('enter the text : ')
res = ''
if (len(text)>=2):
    res += text[0:2]
    res += text[-2:]
    print(res)
elif (len(text)<2):
    print('empty string')
else:
    pass

# Write a Python program to get a string from a given string where all occurrences of its first char have been changed to '$', except the first char itself.
# Sample String : 'restart' , Expected Result : 'resta$t'
text = 'restart'
first = text[0]
text = text.replace(first,'$')
res = first + text[1:]
print(res)

# Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string.
def swap(a,b):
    x1 = a[0:2]
    x2 = a[2:]
    y1 = b[0:2]
    y2 = b[2:]
    res1 = x1 + y2
    res2 = y1 + x2
    print(res2 + " " +  res1)
swap('hai','hello')

# Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If the given string already ends with 'ing' then add 'ly' instead. If the string length of the given string is less than 3, leave it unchanged
text = input('enter the string : ')
if text[-3:] == 'ing' and len(text) > 2:
    print(text + 'ly')
elif text[-3:] != 'ing' and len(text) > 2:
    print(text + 'ing')
else:
    print(text)

# swap comma and dot in string
num = '192,156.47.8388,8389.8858,33.555,090,55.66,444.55'
res1 = num.replace(',','comma')
res1 = res1.replace('.',',')
res1 = res1.replace('comma','.')
print(res1)
print(num)
### ANOTHER METHOD
num = '192.168.4.222,808,45'
res = ''
for i in num:
    if i == '.':
        i = ','
    elif i == ',':
        i = '.'
    res += i
print(res)

# convert str to list
s = 'hai'
print(list(s))

# count and display vowels in string
text = input('enter the text : ')
l = ''
for i in text:
    if i in ('a','e','i','o','u'):
        l += i
print(l)
print(len(l))

# swap lower and uppercase in string
text = input('enter the text : ')
res = ''
for i in text:
    if i.isupper():
        i = i.lower()
    elif i.islower():
        i = i.upper()
    else:
        pass
    res += i
print(res)
######### ANOTHER METHOD
print(text.swapcase())

#  Write a Python function to reverses a string if it's length is a multiple of 4
text = input('enter the text : ')
if(len(text) % 4 == 0):
    print(text[::-1])
else:
    print(text)

# remove the nth index of character in string
def removee(text,n):
    text = input('enter the text : ')
    n = int(input('enter the index number : '))
    return text[:n] + text[n+1:]
print(removee('text','n'))

# first and last character exchanged in string
text = input('enter the text : ')
print(text[-1] + text[1:-1] + text[0])

# prints the unique words in sorted form from a comma separated sequence of words
text = input('enter the text : ').split(",")
li = []
for i in text:
    if i not in li:
        li.append(i)
sort = sorted(li)
print(','.join(sort))
######## ANOTHER METHOD
print(','.join(sorted(list(set(text)))))

# insert string in the middle of another string
def insertt(a,b):
    mid = len(a) // 2
    res = a[0:mid] + b + a[mid:]
    return res
print(insertt('[[]]','python'))
print(insertt('<<>>','HTML'))
print(insertt('{{}}','dictonary'))   