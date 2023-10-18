string = input()
input_string = string.lower().replace(" ", "")

if input_string == input_string[::-1]:
    print(1)
else:
    print(0)