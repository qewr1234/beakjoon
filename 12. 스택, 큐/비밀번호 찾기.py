import sys
input = sys.stdin.readline
N, M = map(int, input().split())
add = {}
for i in range(N):
    website_1, ps = input().split()
    add[website_1] = ps
for i in range(M):
    print(add[input().rstrip()])