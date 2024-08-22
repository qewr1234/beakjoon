N = int(input())
first_list = list(map(int, input().split()))
first_count = {}
for num in first_list:
    if num in first_count:
        first_count[num] += 1
    else:
        first_count[num] = 1
M = int(input())
second_list = list(map(int, input().split()))
result = [first_count[num] if num in first_count else 0 for num in second_list]
print(" ".join(map(str, result)))