###########################
#                         #
# 피보나치 수열에서 동적계획법 #
# Python                  #
###########################

import time
memo = [0 for i in range(100)]
tabu = [0 for j in range(100)]


def piv_rec(N):
    if N <= 1:
        return N
    else:
        return piv_rec(N-1) + piv_rec(N-2)


def piv_dp_memo(N):
    global memo
    if N <= 1:
        memo[N] = N
    if memo[N] != 0:
        return memo[N]
    if N >= 2:
        memo[N] = piv_dp_memo(N-1) + piv_dp_memo(N-2)
    return memo[N]


def piv_dp_tabu(N):
    global tabu
    tabu[0] = 0
    tabu[1] = 1
    if tabu[N] == 0:
        for i in range(2, N+1):
            tabu[i] = tabu[i-1] + tabu[i-2]
    return tabu[N]


N = int(input("N번째 피보나치 수열 N: "))

print('재귀 사용')
t_start = time.time()
print('결과: {}, 걸린 시간: {}'.format(piv_rec(N), time.time() - t_start))
print()

print('DP 사용(Memoization)')
t_start = time.time()
print('결과: {}, 걸린 시간: {}'.format(piv_dp_memo(N), time.time() - t_start))
# print(memo[:N+1:])
print()

print('DP 사용(Tabulation)')
t_start = time.time()
print('결과: {}, 걸린 시간: {}'.format(piv_dp_tabu(N), time.time() - t_start))
# print(tabu[:N+1:])
