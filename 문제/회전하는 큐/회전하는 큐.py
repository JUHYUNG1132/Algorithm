
N, M = map(int, input("").split(" "))

dq = [i for i in range(1, N+1)]

work = 0

for target in map(int, input("").split(" ")):
    idx = dq.index(target)
    work += min(idx, len(dq) - idx)
    dq = dq[idx + 1::] + dq[:idx:]

print(work)