# sol 1, 성공, 53356KB, 236ms
from collections import deque
N = int(input())

queue = deque([x for x in range(1, N+1)])
while(len(queue) != 1):
    queue.popleft()
    queue.append(queue.popleft())
print(*queue)