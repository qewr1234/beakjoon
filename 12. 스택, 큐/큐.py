from collections import deque
import sys

class Queue:
    def __init__(self):
        self.queue = deque()

    def push(self, x):
        self.queue.append(x)

    def pop(self):
        if self.queue:
            return self.queue.popleft()
        else:
            return -1

    def size(self):
        return len(self.queue)

    def empty(self):
        return 1 if not self.queue else 0

    def front(self):
        if self.queue:
            return self.queue[0]
        else:
            return -1

    def back(self):
        if self.queue:
            return self.queue[-1]
        else:
            return -1

# 명령어를 처리할 함수
def process_commands(commands):
    queue = Queue()
    results = []

    for command in commands:
        if command.startswith("push"):
            _, x = command.split()
            queue.push(int(x))
        elif command == "pop":
            results.append(queue.pop())
        elif command == "size":
            results.append(queue.size())
        elif command == "empty":
            results.append(queue.empty())
        elif command == "front":
            results.append(queue.front())
        elif command == "back":
            results.append(queue.back())

    return results

# 입력 예시 처리
if __name__ == "__main__":
    input = sys.stdin.read
    commands = input().strip().split("\n")
    
    results = process_commands(commands)
    for result in results:
        print(result)