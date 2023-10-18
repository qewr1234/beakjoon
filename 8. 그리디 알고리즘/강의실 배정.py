import heapq # heapq 모듈을 import

n = int(input()) # 강의 수를 입력받음

# 각각의 강의에 대한 시작 시간과 종료 시간을 입력받고 리스트에 저장
lecture_list = [list(map(int, input().split())) for _ in range(n)]

# 강의의 종료 시간을 기준으로 오름차순으로 정렬
lecture_list.sort()

lecture_queue = [] # 강의 종료 시간을 저장할 우선순위 큐를 초기화
heapq.heappush(lecture_queue, lecture_list[0][1]) # 첫 번째 강의의 종료 시간을 큐에 넣음

for i in range(1, n):
    # 현재 강의의 시작 시간이 큐의 가장 일찍 끝나는 강의의 종료 시간보다 작으면
    # 새로운 강의실이 필요하므로 종료 시간을 큐에 추가합니다.
    if lecture_list[i][0] < lecture_queue[0]:
        heapq.heappush(lecture_queue, lecture_list[i][1])
    else:
        # 현재 강의의 시작 시간이 큐의 가장 일찍 끝나는 강의의 종료 시간과 같거나 크다면
        # 해당 강의실을 재사용할 수 있으므로 큐에서 가장 일찍 끝나는 강의를 빼고
        # 현재 강의의 종료 시간을 큐에 추가합니다.
        heapq.heappop(lecture_queue)
        heapq.heappush(lecture_queue, lecture_list[i][1])

print(len(lecture_queue))

