from collections import deque
import sys
import copy

input = sys.stdin.readline

d = [[-1, 0], [1, 0], [0, -1], [0, 1]]

def BFS():
    queue = deque()
    test_map = copy.deepcopy(lab_map)
    for i in range(n):
        for j in range(m):
            if test_map[i][j] == 2:
                queue.append((i, j))

    while queue:
        r, c = queue.popleft()
        
        for i in range(4):
            dr = r+d[i][0]
            dc = c+d[i][1]
            
            if (0 <= dr < n) and (0 <= dc < m):
                if test_map[dr][dc] == 0:
                    test_map[dr][dc] = 2
                    queue.append((dr, dc))
                    
    global result
    cnt = 0
    for i in range(n):
        for j in range(m):
            if test_map[i][j] == 0:
                cnt += 1
                
    result = max(result, cnt)
    
def make_wall(cnt):
    if cnt == 3:
        BFS()
        return
    
    for i in range(n):
        for j in range(m):
            if lab_map(m):
                if lab_map[i][j] == 0:
                    lab_map[i][j] = 1
                    make_wall(cnt + 1)
                    lab_map[i][j] = 0
                    
n, m = map(int, input().split())
lab_map = [list(map(int, input().split())) for _ in range(n)]

result = 0
make_wall(0)

print(result)