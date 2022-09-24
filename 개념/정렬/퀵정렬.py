"""
기본적인 퀵 정렬
임의로 피벗을 정하고,
피벗보다 작은 수들은 왼쪽으로
큰 수들은 오른쪽으로 보내며 재귀
최악의 경우, O(n^2)이 되며, 리스트 복사로 인해 메모리 많이 먹음
"""

import lst_tool

def qsort(lst):
    if not lst:
        return []
    else:
        pivot = lst[0]
        lesser = qsort([x for x in lst[1:] if x < pivot])
        greater = qsort([x for x in lst[1:] if x >= pivot])
        return lesser + [pivot] + greater


s = list(lst_tool.mklst(20000, -10000, 10000))

print("quicksort = {}".format(lst_tool.avg_time(qsort, s, 30)))

print("sorted    = {}".format(lst_tool.avg_time(sorted, s, 30)))
