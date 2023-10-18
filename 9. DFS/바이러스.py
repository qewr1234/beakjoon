num = int(input()) # 컴퓨터의 수
v = int(input()) # 연결선의 수

graph = [[] for i in range(num+1)] # 그래프 초기화

visited = [False]*(num+1) # 방문한 컴퓨터인지 표시 

for i in range(v): # 그래프 생성
    a, b = map(int, input().split())
    graph[a] += [b] # a에 b연결
    graph[b] += [a] # b에 a연결 -> 양방향
    
def DFS(v):
    visited[v] = 1
    for j in graph[v]:
        if visited[j] == 0:
            DFS(j)
            
DFS(1)
print(sum(visited)-1)