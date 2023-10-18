# 어렵다... 이게 골드2라니... 아직 한참 남았다... 
# heapq를 사용해서 가방안에 넣는것 까진 생각했는데 보석 분류하는걸 못하겠다...

import sys
import heapq

N, K = map(int,input().split())
jewel_list = []
pocket_list = []

for _ in range(N):
    jewel_list.append([int(x) for x in sys.stdin.readline().rstrip().split()])
for _ in range(K):
    pocket_list.append(int(sys.stdin.readline().rstrip()))
jewel_list.sort()
pocket_list.sort()

ans = 0
can_put_in = []

for pocket in pocket_list:
    while jewel_list:
        if pocket >= jewel_list[0][0]:
            heapq.heappush(can_put_in, -jewel_list[0][1])
            heapq.heappop(jewel_list)
        else:
            break

    if can_put_in:
        ans += -heapq.heappop(can_put_in)
    else:
        if not jewel_list:
            break

print(ans)