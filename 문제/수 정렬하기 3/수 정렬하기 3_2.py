# sol 2 실패, 시간 초과
N = int(input())

num = [0] * 10001

for i in range(N):
    temp = int(input())
    num[temp-1] = num[temp-1] + 1

for i in range(10001):
    if num[i] != 0:
        for j in range(num[i]):
            print(i+1)
