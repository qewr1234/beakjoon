class Stack:
    def __init__(self):
        self.stack = []

    def push(self, x):
        self.stack.append(x)

    def pop(self):
        if not self.stack:
            return -1
        else:
            return self.stack.pop()

    def size(self):
        return len(self.stack)

    def empty(self):
        return 1 if not self.stack else 0

    def top(self):
        if not self.stack:
            return -1
        else:
            return self.stack[-1]

# 명령어를 처리할 함수
def process_commands(commands):
    stack = Stack()
    results = []

    for command in commands:
        if command.startswith("push"):
            _, x = command.split()
            stack.push(int(x))
        elif command == "pop":
            results.append(stack.pop())
        elif command == "size":
            results.append(stack.size())
        elif command == "empty":
            results.append(stack.empty())
        elif command == "top":
            results.append(stack.top())

    return results

# 입력 예시 처리
if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    commands = input().strip().split("\n")
    
    results = process_commands(commands)
    for result in results:
        print(result)