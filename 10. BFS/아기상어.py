from collections import deque

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]

pos = []
cnt = 0

for i in range(n):
    for j in range(n):
        if graph[i][j] == 9:
            pos.append(i)
            pos.append(j)
            
def BFS(x, y):
    visited = [[0]*n for _ in range(n)]
    queue = deque([[x,y]])
    cand = []

    visited[x][y] = 1
    
    while queue:
        r, c = queue.popleft()
        
        for idx in range(4):
            dr, dc = r + dx[idx], c + dy[idx]
            
            if 0 <= dr and dr < n and 0 <= dc and dc < n and visited[dr][dc] == 0:
                if graph[x][y] > graph[dr][dc] and graph[dr][dc] != 0:
                    visited[dr][dc] =  visited[r][c] + 1
                    cand.append((visited[dr][dc] - 1, dr, dc))
                elif graph[x][y] == graph[dr][dc]:
                    visited[dr][dc] =  visited[r][c] + 1
                    queue.append([dr,dc])
                elif graph[dr][dc] == 0:
                    visited[dr][dc] =  visited[r][c] + 1
                    queue.append([dr,dc])
    return sorted(cand, key = lambda x: (x[0], x[1], x[2]))

r, c = pos
size = [2, 0]
while True:
    graph[r][c]  = size[0]
    cand = deque(BFS(r, c))
    if not cand:
        break
    step, xx, yy = cand.popleft()
    cnt += step
    size[1] += 1
    
    if size[0] == size[1]:
        size[0] += 1
        size[1] = 0
        
    graph[r][c] = 0
    r, c = xx, yy
    
print(cnt) 