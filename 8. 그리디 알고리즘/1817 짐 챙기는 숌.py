N, M = map(int, input().split())
if N == 0:
    print(0)
else:
    boxes = list(map(int, input().split()))
    print(boxes)
    total_weight = 0
    cnt = 1

    for box in boxes:
        if box + total_weight <= M:
            total_weight += box
        else:
            total_weight = box
            cnt += 1

    print(cnt)