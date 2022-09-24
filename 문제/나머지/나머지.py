# sol 1, 통과, 30840KB, 72ms
a = list()
for i in range(10):
    a.append(int(input()) % 42)
a = set(a)
print(len(a))