# sol 1, 통과, 메모리 46816KB, 시간 748ms
N_A = int(input())

A = list(map(int, input().split(" ")))
A.sort()

N_M = int(input())

M = list(map(int, input().split(" ")))

def b_search(A, start, end, target):
    mid = (start+end)//2
    if abs(start-end) <= 1:
        if A[mid] == target:
            return 1
        else:
            return 0
    elif A[mid] < target:
        return b_search(A, mid, end, target)
    elif A[mid] > target:
        return b_search(A, start, mid, target)
    elif A[mid] == target:
        return 1

for i in range(N_M):
    print(b_search(A, 0, N_A, M[i]))
