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
    