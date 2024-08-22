import sys
input = sys.stdin.readline
N, M = map(int, input().split())
name1 = []
name2 = []
for i in range(N):
    x = input()
    name1.append(x)
for i in range(M):
    y = input()
    name2.append(y)

answer = list(set(name1) & set(name2))
answer.sort()
print(len(answer))
print(''.join(answer), end = '')
