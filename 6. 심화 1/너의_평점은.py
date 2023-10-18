sum = 0
total_score = 0
grade_mapping = {'A+':4.5,'A0':4.0,'B+':3.5, 'B0':3.0, 'C+':2.5, 'C0':2.0, 'D+':1.5, 'D0':1.0, 'F':0.0} # 등급과 해당 가중치 매핑

for _ in range(20):
    subject, score, grade_letter = input().split()
    score = float(score) # 문자열을 실수로 변환
    
    if grade_letter == "P": # 등급이 P라면 0
        sum += 0
    else:
        sum += score
        total_score += score * grade_mapping.get(grade_letter, 0) # 등급에 해당하는 가중치 가져오기
        
print(total_score/sum)
