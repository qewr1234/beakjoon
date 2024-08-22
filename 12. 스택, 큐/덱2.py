from collections import deque
import sys
N = int(sys.stdin.readline().strip())
dq = deque()
for i in range(N):
    command = sys.stdin.readline().split()
    if command[0] == "1":
        dq.appendleft(command[1])

    elif command[0] == "2":
        dq.append(command[1])

    elif command[0] == "3":
        if len(dq) == 0:
            print(-1)
        else:
            print(dq[0])
            dq.popleft()
    
    elif command[0] == "4":
        if len(dq) == 0:
            print(-1)
        else:
            print(dq[len(dq) - 1])
            dq.pop()
        
    elif command[0] == "5":
        print(len(dq))

    elif command[0] == "6":
        if len(dq) == 0:
            print(1)
        else:
            print(0)
    
    elif command[0] == "7":
        if len(dq) == 0:
            print(-1)
        else:
            print(dq[0])

    elif command[0] == "8":
        if len(dq) == 0:
            print(-1)
        else:
            print(dq[len(dq) - 1])