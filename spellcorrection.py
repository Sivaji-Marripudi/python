from textblob import TextBlob
a = input('enter the text : ')
print(str(a))
b = TextBlob(a)
print(str(b.correct()))