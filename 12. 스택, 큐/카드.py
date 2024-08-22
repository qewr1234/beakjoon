import sys
input = sys.stdin.readline
N = int(input())
count = {}
for i in range(N):
    card = int(input())
    if card in count:
        count[card] += 1
    else:
        count[card] = 1
result = sorted(count.items(), key = lambda x : (-x[1], x[0]))
print(result[0][0])