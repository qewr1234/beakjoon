N = int(input())
Time = []
result = []

for i in range(N):
    start, end = list(map(int,input().split()))
    Time.append((start, end))
    
Time = sorted(Time, key=lambda a:a[0])
Time = sorted(Time, key=lambda a:a[1])
 
last = 0
cnt = 0

for i, j in Time:
    if i >= last:
        cnt += 1
        last = j   
print(cnt)