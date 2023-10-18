a = input()
upper_case_string = a.upper() # 알파벳 소문자를 대문자로 변경
cnt = {} # 알파벳 빈도를 저장하기 위한 딕셔너리를 초기화

for char in upper_case_string:
    if char.isalpha(): # 알파벳인 경우에만 처리함
        if char in cnt:
            cnt[char] += 1 # 이미 딕셔너리에 있는 알파벳의 빈도를 증가
        else:
            cnt[char] = 1 # 딕셔너리에 알파벳을 추가하고 빈도를 1로 설정
            
max_count = max(cnt.values()) # 가장 많이 사용된 알파벳의 빈도를 찾음
        
Most = [char for char, count in cnt.items() if count == max_count] # 가장 많이 사용된 알파벳을 리스트에 저장

if len(Most) == 1:
    print(Most[0])
else:
    print("?")

