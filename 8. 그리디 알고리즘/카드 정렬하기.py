import heapq

num = int(input())
Card = []

for _ in range(num):
    heapq.heappush(Card, int(input()))
    
if len(Card) == 1:
    print(0)
    
else:
    cnt = 0
    while len(Card) > 1:
        temp_1 = heapq.heappop(Card)
        temp_2 = heapq.heappop(Card)
        cnt += temp_1 + temp_2
        heapq.heappush(Card, temp_1 + temp_2)
        
    print(cnt)
