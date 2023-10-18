arr_1 = [int(x) for x in input().split()] # arr_1을 직접 입력
arr_2 = [1, 1, 2, 2, 2, 8]

result = [str(a-b) for a, b in zip(arr_2, arr_1)] # 두 리스트의 각 요소를 뺀 결과를 계산
result_str = " ".join(result) # 결과 문자열을 공백으로 구분하여 하나의 문자열로 만듬

print(result_str)


""" # 더 쉬운 코드
chess = [1, 1, 2, 2, 2, 8] # 고정된 말의 수

a = list(map(int, input().split()))

for i in ragne(6):
    print(chess[i] - a[i], end = ' ')
    
"""