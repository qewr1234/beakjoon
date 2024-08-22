import sys
stack = []
k = int(sys.stdin.readline())
for _ in range(k):
    count = int(input())
    if count == 0:
        stack.pop()
    else:
        stack.append(count)
print(sum(stack))

