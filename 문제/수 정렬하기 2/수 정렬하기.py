import sys
N = int(sys.stdin.readline())
s = list()

def qsort(lst):
    if lst == []:
        return []
    else:
        pivot = lst[0]
        lesser = qsort([x for x in lst[1:] if x < pivot])
        greater = qsort([x for x in lst[1:] if x >= pivot])
        return lesser + [pivot] + greater

for i in range(N):
    s.append(int(sys.stdin.readline()))

print(*qsort(s), sep="\n")
