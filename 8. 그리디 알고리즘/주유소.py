City = int(input())
Distance = list(map(int, input().split()))
Petroleum = list(map(int, input().split()))

result = 0
result += Distance[0] * Petroleum[0]

min_cost = Petroleum[0]

for i in range(1, City-1):
    if min_cost > Petroleum[i]:
        min_cost = Petroleum[i]
        
    result += min_cost*Distance[i]
        
print(result)


