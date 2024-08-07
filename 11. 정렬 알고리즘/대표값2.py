arr = []

for i in range(5):
    a = int(input())
    arr.append(a)

arr.sort()
print(int(sum(arr)/5))
print(arr[2])
