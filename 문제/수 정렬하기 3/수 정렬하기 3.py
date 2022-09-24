# sol 1 실패, 메모리 초과
import time

t_start = time.time()

N = int(input())
lst = [0]*N

for i in range(N):
    lst[i] = int(input())

size = len(lst) - 1
for i in range(size):
    for j in range(size-i):
        if lst[j] > lst[j+1]:
            lst[j], lst[j+1] = lst[j+1], lst[j]

for i in range(size + 1):
    print(lst[i])

print(time.time()-t_start)
