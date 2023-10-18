num = int(input())

Cup_Holder = input().replace(" ", "")
cnt = 1

i = 0

while i < len(Cup_Holder):
    if Cup_Holder[i] == 'S':
        cnt += 1
        i += 1
    elif i < len(Cup_Holder) - 1 and Cup_Holder[i] == 'L' and Cup_Holder[i + 1] == 'L':
        cnt += 1
        i += 2
    else:
        i += 1
    
if cnt > num:
    cnt -= 1
    
print(cnt)
    