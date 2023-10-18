import heapq

def minimum_comparison(Card_Size):
    heapq.heapify(Card_Size)
    
    total_comparison = 0
    
    while len(Card_Size) > 1:
        a = heapq.heappop(Card_Size)
        b = heapq.heappop(Card_Size)
        combined = a + b
        total_comparison += combined
        heapq.heappush(Card_Size, combined)
        
    return total_comparison

num = int(input())
Card_Sizes = []

for _ in range(num):
    Size = int(input())
    Card_Sizes.append(Size)

result = minimum_comparison(Card_Sizes)
print(result)