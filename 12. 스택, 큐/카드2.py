from collections import deque

def last_card(N):
    queue = deque(range(1, N + 1))  # 1부터 N까지의 숫자를 큐에 넣음
    
    while len(queue) > 1:
        queue.popleft()  # 제일 위에 있는 카드를 버림
        queue.append(queue.popleft())  # 다음 카드를 제일 아래로 이동
    
    return queue[0]  # 마지막으로 남은 카드를 반환

# N을 입력받고, 마지막 남는 카드를 출력
N = int(input())
print(last_card(N))