from typing import MutableSequence
import random
import time

def shaker_sort(a: MutableSequence) -> None:
    left = 0
    right = len(a) - 1
    last = right
    while left < right:
        for j in range(right, left, -1):
            if a[j - 1] > a[j]:
                a[j - 1], a[j] = a[j], a[j - 1]
                last = j
        left = last
        
        for j in range(left, right):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                last = j
        right = last
        
def print_partitioned_list(lst):
    for i in range(0, len(lst), 10):
        print(lst[i:i+10])

if __name__ == '__main__':
    # 1부터 1,000,000 사이의 수 중에서 무작위로 1,000,000개의 수를 선택
    x = random.sample(range(1, 1000001), 10000)
    
    print("정렬 전 첫 20개:")
    print_partitioned_list(x[:20])
    print("정렬 전 마지막 20개:")
    print_partitioned_list(x[-20:])
    
    start_time = time.time()
    shaker_sort(x)
    end_time = time.time()
    
    elapsed_time = end_time - start_time
    
    print("정렬에 걸린 시간: {:.2f} 초".format(elapsed_time))
    
    print("정렬 후 첫 20개:")
    print_partitioned_list(x[:20])
    print("정레 후 마지막 20개:")
    print_partitioned_list(x[-20:])