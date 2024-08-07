import random
import time
from typing import MutableSequence

def binary_insertion_sort(a: MutableSequence) -> None:
    n = len(a)
    for i in range(1, n):
        key = a[i]
        pl = 0
        pr = i - 1
        
        while True:
            pc = (pl + pr) // 2
            if pl > pr:
                pd = pl
                break
            if a[pc] == key:
                pd = pc
                break
            elif a[pc] < key:
                pl = pc + 1
            else:
                pr = pc - 1
        
        for j in range(i, pd, -1):
            a[j] = a[j - 1]
        a[pd] = key

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
    binary_insertion_sort(x)
    end_time = time.time()
    
    elapsed_time = end_time - start_time
    
    print("정렬에 걸린 시간: {:.2f} 초".format(elapsed_time))
    
    print("정렬 후 첫 20개:")
    print_partitioned_list(x[:20])
    print("정레 후 마지막 20개:")
    print_partitioned_list(x[-20:])