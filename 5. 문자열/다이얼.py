dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
a = input()
cnt = 0
for j in range(len(a)):
    for i in dial:
        if a[j] in i:
            cnt += dial.index(i)+3
print(cnt)
