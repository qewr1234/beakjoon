N = int(input())
person = []

for i in range(N):
    data = input()
    age, name = data.split()
    age = int(age)
    person.append((age, name, i))

# 나이순으로 정렬하되, 나이가 같으면 입력된 순서대로 정렬
# 첫 번째 정렬 기준은 나이 (x[0])
# 두 번째 정렬 기준은 입력된 순서 (x[2])    
people_sorted = sorted(person, key=lambda x: (x[0], x[2]))
for person in people_sorted:
    print(f"{person[0]} {person[1]}")
    
