N, M, K = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
first = data[N - 1]
second = data[N - 2]


cnt = int(M / (K+1)) * K
cnt += M % (K + 1)

result = 0
result += cnt * first
result += (M - cnt) * second

print(result)
    