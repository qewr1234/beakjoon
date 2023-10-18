"""
Time = {'A':300, 'B':60, 'C':10}

micro = int(input())
arr = [0 ,0, 0]

while 1:
    if micro >= Time['A']:
        micro = micro - Time['A']
        arr[0] += 1
    elif micro >= Time['B'] and micro < Time['A']:
        micro = micro - Time['B']
        arr[1] += 1
    elif micro >= Time['C'] and micro < Time['B']:
        micro = micro - Time['C']
        arr[2] += 1
    else:
        print("-1")
        break
    if micro == 0:
        print(arr[0], arr[1], arr[2])
        break        
"""

Time = {'A': 300, 'B': 60, 'C': 10}

micro = int(input(""))
arr = [0, 0, 0]

for key in ['A', 'B', 'C']:
    while micro >= Time[key]:
        micro -= Time[key]
        arr['ABC'.index(key)] += 1

if micro == 0:
    print(*arr)
else:
    print("-1")