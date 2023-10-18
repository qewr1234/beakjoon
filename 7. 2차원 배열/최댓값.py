matrix = []
for _ in range(9):
    row = list(map(int, input().split()))
    matrix.append(row)
    
max_value = matrix[0][0]
max_row = 0
max_col = 0

for row_index, row in enumerate(matrix):
    for col_index, element in enumerate(row):
        if element > max_value:
            max_value = element
            max_row = row_index
            max_col = col_index 
            
print(max_value)
print(max_row + 1, max_col + 1)