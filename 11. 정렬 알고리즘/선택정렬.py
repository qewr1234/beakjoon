import random
import time
from typing import MutableSequence

def selection_sort(a: MutableSequence) -> None:
    n = len(a)
    
    for i in range(n - 1):
        min = i # 정렬할 부분에서 가장 작은 원소와 인덱스
        for j in range(i + 1, n):
            if a[j] < a[min]:
                min = j
        a[i], a[min] = a[min], a[i] # 정렬할 부분에서 맨 앞의 원소와 가장 작은 원소를 교환

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
    selection_sort(x)
    end_time = time.time()
    
    elapsed_time = end_time - start_time
    
    print("정렬에 걸린 시간: {:.2f} 초".format(elapsed_time))
    
    print("정렬 후 첫 20개:")
    print_partitioned_list(x[:20])
    print("정레 후 마지막 20개:")
    print_partitioned_list(x[-20:])