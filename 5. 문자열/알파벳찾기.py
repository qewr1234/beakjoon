import sys

text = sys.stdin.readline()
abc ='abcdefghijklmnopqrstuvwxyz'

for i in abc:
    if i in text:
        print(text.index(i), end= ' ')
    else:
        print( -1, end =' ')