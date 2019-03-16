from itertools import permutations
import nltk
nltk.download('words')
from nltk.corpus import words
s=input()
perm=permutations(s)
b=[]
for i in list(perm):
    b.append((''.join(i)))
for i in b:
    while(i in words.words()):
        print(i)
        break