N, K = map(int, input().split())
Coin = []
cnt = 0

for i in range(N):
    Coin.append(int(input()))

Coin.sort(reverse=True)

for i in Coin:
    if K > i:
        cnt += K // i # coin 몫만큼 더하기 
        K %= i # 나머지 할당
        if K < 0: # 만약 K가 0이면 반복문을 탈줄
            break
    
print(cnt)