A, B, C = map(int, input().split())

if A >= B and A >= C:
    second = max(B, C)
elif B >= A and B >= C:
    second = max(A, C)
elif C >= A and C >= B:
    second = max(A, B)
    
print(second)