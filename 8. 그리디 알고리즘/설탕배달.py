Suger = {'A':5, 'B':3}
cnt = 0

num = int(input())

while num >= 0:
    if num % Suger['A'] == 0:
        cnt += (num//Suger['A'])
        print(cnt)
        break
    num  -= Suger['B']
    cnt += 1
else:
    print(-1)