from collections import deque
import sys
input = sys.stdin.readline

dx = [-1, 1]

#bfs
def bfs():
    q = deque()
    q.append(N)
    while q:
        x = q.popleft()
        if x == K:
            print(distance[x])
            break
        for nx in (x - 1, x + 1, x * 2):
            if 0 <= nx <= MAX and not distance[nx]:
                distance[nx] = distance[x] + 1
                q.append(nx)

        

            

#구현
MAX = 10 ** 6
distance = [0] * (MAX + 1)
N, K = map(int, input().split())
bfs()

