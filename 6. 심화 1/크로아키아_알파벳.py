croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
input_string = input()


for i in croatia:
    input_string = input_string.replace(i, '*')
    
print(len(input_string))


