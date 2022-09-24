"""
버블 정렬
두 인접한 원소를 비교해가며 정렬
항상 첫번쨰 원소에서 시작해
왼쪽의 값이 크면 둘의 위치를 바구고, 아니면 그대로 둔다
시간 복잡도는 O(N^2)으로 크지만, 공간 복잡도가 O(n)으로 작다
"""

import lst_tool

def bsort(lst):
    size = len(lst) - 1

    for i in range(size):
        for j in range(size-i):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]


s = list(lst_tool.mklst(1000, -10000, 10000))

print("bubblesort = {}".format(lst_tool.avg_time(bsort, s, 30)))

print("sorted     = {}".format(lst_tool.avg_time(sorted, s, 30)))
