#Import textblob
from textblob import TextBlob

a = TextBlob("")

#Using Textblob.correct() method
a = a.correct()

print(a)
