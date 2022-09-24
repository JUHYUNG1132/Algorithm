# sol 1, 실패, 메모리 초과
import sys

n, m = map(int, sys.stdin.readline().split(" "))
res = [{x}for x in range(n+1)]

for i in range(m):
    op, a, b = map(int, sys.stdin.readline().split(" "))
    if op:
        if b in res[a]:
            print("YES")
        else:
            print("NO")
    
    else:
        #res[a].add(b)
        map(res[a].add, res[b])
        # res[a].add(*res[b])