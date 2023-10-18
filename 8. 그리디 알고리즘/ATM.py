num = int(input())
People = [0]*num
result = 0

People = list(map(int,input().split()))

People.sort()

for i in range(1, num+1):
    result += sum(People[0:i]) #리스트의 0번째 수 부터 i번째 수 까지 더함
    
print(result, end = " ")
    