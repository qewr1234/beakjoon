nums = list(map(int, str(input()))) # 숫자를 하나 하나씩 받을 수 있다!
nums.sort(reverse=True)
for i in nums:
    print(i, end = '')