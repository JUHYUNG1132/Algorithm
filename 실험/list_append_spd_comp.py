"""
리스트 원소 추가시
속도 비교
"""

import time
import random

N = 10000000
t = time.time()
lst = [0]*N
for i in range(N):
    lst[i] = i # random.randint(0, 100)
print(time.time()-t)

t = time.time()
lst = list()
for i in range(N):
    lst.append(i) # random.randint(0, 100))
print(time.time()-t)

t = time.time()
lst = list()
for i in range(N):
    lst.insert(-1, i) # random.randint(0, 100))
print(time.time()-t)

"""
list 삽입 속도
  DP < append < insert
 (빠름)          (느림)
"""
