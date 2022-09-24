"""
sorted()와 sort()
함수 속도 비교
"""
import time
t = time.time()

lst = [i for i in range(100000000, 0, -1)]
sorted(lst)
print(time.time()-t)

t = time.time()
lst.sort()
print(time.time() - t)
"""
메소드가 훨씬 더 빠름
"""
