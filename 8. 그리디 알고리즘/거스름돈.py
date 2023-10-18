exp = {'A':5, 'B':2}
num = int(input())
cnt = 0

while True:
    if num % exp['A'] == 0:
        cnt += num // exp['A']
        break
    
    else:
        num -= 2
        cnt += 1
        
    if num < 0:
        break
    
if num < 0:
    print(-1)
else:
    print(cnt)