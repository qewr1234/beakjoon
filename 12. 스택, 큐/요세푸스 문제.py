from collections import deque
def josephus_permutation(n, k):
    people = deque(range(1, n+1))
    result = []
    while people:
        people.rotate(-k+1)
        result.append(people.popleft())
    return result
n, k = map(int, input().split())
josephus_sequence = josephus_permutation(n, k)
print(f'<{", ".join(map(str, josephus_sequence))}>')