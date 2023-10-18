N, M = map(int, input().split())
arr_1 = []
arr_2 = []
result = []

for _ in range(N):
    row_A = list(map(int, input().split()))
    arr_1.append(row_A)
    
for _ in range(N):
    row_B = list(map(int, input().split()))
    arr_2.append(row_B)
    
for i in range(N):
    row_result = []
    for j in range(M):
        sum = arr_1[i][j] + arr_2[i][j]
        row_result.append(sum)
    result.append(row_result)
    
for row in result:
    print(*row)
