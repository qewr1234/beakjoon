import sys
sys.setrecursionlimit(10**8)
input=sys.stdin.readline
def dfs(i,idx,graph):
    for j in graph[idx]:
        if not check[i][j]:
            check[i][j] = 1
            check[j][i] = 1
            dfs(i,j,graph)
N,M=map(int, input().split())
graph=[[] for _ in range(N)]
for _ in range(M):
    a,b=map(int,input().split())
    if b-1 not in graph[a-1]:
        graph[a-1].append(b-1)
check=[[0 for _ in range(N)] for _ in range(N)]
for i in range(N):
    check[i][i]=1
    dfs(i,i,graph)
result=0
for row in check:
    if row==[1]*N:
        result += 1
print(result) 