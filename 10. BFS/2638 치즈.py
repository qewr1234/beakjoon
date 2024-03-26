from collections import deque
import sys

input = sys.stdin.readline

N, M = map(int, input().split())
graph = [list(map(int,input().split())) for _ in range(N)]

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

#bfs
def bfs():
    q = deque()
    q.append([0, 0])
    visited[0][0] = 1
    while q:
        x, y = q.popleft()
        for idx in range(4):
            newX = x + dx[idx]
            newY = y + dy[idx]

            if 0 <= newX < N and 0 <= newY < M and visited[newX][newY] == 0:
                if graph[newX][newY] >= 1:
                    graph[newX][newY] += 1
                else:
                    visited[newX][newY] = 1
                    q.append([newX, newY])

#구현
time = 0
while 1:
    visited = [[0] * M for _ in range(N)]
    bfs()
    flag = 0

    for i in range(N):
        for j in range(M):
            if graph[i][j] >= 3:
                graph[i][j] = 0
                flag = 1
            elif graph[i][j] == 2:
                graph[i][j] = 1
    if flag == 1:
        time += 1
    else:
        break

print(time)