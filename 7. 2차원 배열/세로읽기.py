text = []

for _ in range(5):
    row = input().strip()
    text.append(row)

max_length = max(len(row) for row in text)

result = ""

for i in range(max_length):
    for row in text:
        if i < len(row):
            result += row[i]
            
print(result)
