
from collections import deque

N, M, v = map(int, input().split())
                
graph = [[False] * (N + 1) for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b] = True
    graph[b][a] = True
    
visited_dfs = [False]*(N+1)
visited_bfs = [False]*(N+1)

def DFS(v):
    visited_dfs[v] = True
    print(v, end = ' ')
    
    for i in range(1, N+1):
        if not visited_dfs[i] and graph[v][i]:
            DFS(i)
            
def BFS(v):
    queue = deque([v])
    visited_bfs[v] = True
    
    while queue:
        v = queue.popleft()
        print(v, end = ' ')
        
        for i in range(1, N+1):
            if not visited_bfs[i] and graph[v][i]:
                queue.append(i)
                visited_bfs[i] = True

DFS(v)
print()
BFS(v)