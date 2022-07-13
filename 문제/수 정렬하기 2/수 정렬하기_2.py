# sol2, 성공, 메모리 87456, 시간 1392ms
import sys
N = int(sys.stdin.readline())
s = list()

for i in range(N):
    s.append(int(sys.stdin.readline()))

print(*sorted(s), sep="\n")

# ????
# 정렬속도 sorted > quick sort (nlogn) < sort 인가?
