
N, K = map(int,input().split(' '))

values = list()
count = 0
n = 0

for lines in range(N):
    values.append(int(input()))

for i in reversed(range(N)):
    count += K // values[i]
    K = K % values[i]
    if(K == 0):
        break

print(count)