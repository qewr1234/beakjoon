n = int(input())
company = set()
for _ in range(n):
    name, log = input().split()
    if log == "enter":
        company.add(name)
    elif log == "leave":
        company.discard(name)
for name in sorted(company, reverse=True):
    print(name)



