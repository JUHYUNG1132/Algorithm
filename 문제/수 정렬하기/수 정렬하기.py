# sol 1, 통과, 메모리 30840KB, 시간 108ms
N = int(input())
s = set()

for i in range(N):
    s.add(int(input()))
s = sorted(s)

print(*s, sep="\n")