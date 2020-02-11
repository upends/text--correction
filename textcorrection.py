from textblob import TextBlob

file1 = open('correction.txt', 'r')
a = file1.read()

print('Original text:'+str(a))

b=TextBlob(a)

print("corrected text:"+str(b.correct()))
file1.close()

d = open('correction.txt', 'w')
d.write(str(b.correct()))
d.close