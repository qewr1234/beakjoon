import sys

n = int(sys.stdin.readline())
num = [int(sys.stdin.readline()) for _ in range(n)]
num.sort()
for i in range(n):
    print(num[i])
