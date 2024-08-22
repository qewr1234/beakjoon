# 첫 번째 입력 (첫 번째 리스트의 길이와 리스트 요소들)
N = int(input())
first_list = set(map(int, input().split()))  # 리스트를 집합으로 변환
first_count = {}

for num in first_list:
    if num in first_count:
        first_count[num] += 1
    else:
        first_count[num] = 1

# 두 번째 입력 (두 번째 리스트의 길이와 리스트 요소들)
M = int(input())
second_list = list(map(int, input().split()))

# 첫 번째 리스트의 각 요소가 두 번째 리스트에 있는지 확인
result = [1 if num in first_list else 0 for num in second_list]

# 결과 출력
print(" ".join(map(str, result)))