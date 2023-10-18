arr = [] # 빈 리스트 생성
while 1: # 무한 반복
    try:
        line = input() # 입력
        if not line: # 입력이 없을 경우 종료
            break
        arr.append(line) # 입력한 줄을 리스트에 추가
    except EOFError: # EOFError 예외가 발생하면 파일의 끝에 도달
        break

for line in arr: # 출력
    print(line)