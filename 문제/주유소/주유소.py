N = int(input())

dist = tuple(map(int, input().split(' ')))
cost = tuple(map(int, input().split(' ')))

leng = 0
used = 0
bigg = max(cost)
prev = cost[0]

for i in range(N-1):
    if(cost[i] <= prev):
        used += cost[i]*dist[i]
        prev = cost[i]
    else:
        used += prev*dist[i]

print(used)