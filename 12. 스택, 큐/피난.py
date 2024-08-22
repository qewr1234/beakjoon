from collections import deque, defaultdict

def bfs(capacity, source, sink, parent):
    visited = [False] * len(capacity)
    queue = deque([source])
    visited[source] = True

    while queue:
        u = queue.popleft()

        for v in range(len(capacity)):
            if not visited[v] and capacity[u][v] - flow[u][v] > 0:  # 남은 용량이 있는지 확인
                queue.append(v)
                visited[v] = True
                parent[v] = u
                if v == sink:
                    return True
    return False

def edmonds_karp(capacity, source, sink):
    global flow
    flow = [[0] * len(capacity) for _ in range(len(capacity))]
    parent = [-1] * len(capacity)
    max_flow = 0

    while bfs(capacity, source, sink, parent):
        path_flow = float('Inf')
        s = sink

        while s != source:
            path_flow = min(path_flow, capacity[parent[s]][s] - flow[parent[s]][s])
            s = parent[s]

        v = sink
        while v != source:
            u = parent[v]
            flow[u][v] += path_flow
            flow[v][u] -= path_flow
            v = u

        max_flow += path_flow

    return max_flow

def solve(N, M, edges):
    capacity = [[0] * N for _ in range(N)]
    for x, y in edges:
        capacity[x-1][y-1] = 1  # x에서 y로 가는 간선에 대해 용량 1 할당

    return edmonds_karp(capacity, 0, N-1)  # 체크포인트 1번(인덱스 0)에서 N번(인덱스 N-1)까지의 최대 유량

import sys
input = sys.stdin.read
data = input().split()
index = 0
T = int(data[index])
index += 1
results = []

for _ in range(T):
    N = int(data[index])
    M = int(data[index+1])
    index += 2
    edges = []
    for _ in range(M):
        x = int(data[index])
        y = int(data[index+1])
        edges.append((x, y))
        index += 2
    results.append(solve(N, M, edges))

for result in results:
    print(result)