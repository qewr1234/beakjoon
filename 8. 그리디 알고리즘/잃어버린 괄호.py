num = input().split('-') # '-'를 기준으로 수식을 나눈다
result = 0

for i in num[0].split('+'): # '+'를 기준으로 나누고 숫자를 더함
    result += int(i)
    
for i in num[1:]: # 나머지 부분을 처
    for j in i.split('+'): # '-'로 나눈 덩어리를 다시 '+'로 나누고 숫자를 뺌
        result -= int(j)
        
print(result)
