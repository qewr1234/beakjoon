N = int(input())

arr = []

for i in range(N):
    [x, y] = map(int, input().split())
    arr.append([x, y])
    
arr_sort = sorted(arr)

for i in range(N):
    print(arr_sort[i][0], arr_sort[i][1])    
