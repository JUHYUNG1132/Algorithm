# sol 1, 통과, 메모리 226756KB, 시간 5896ms

max_n, max_w = map(int, input().split(" "))

item_lst = [(0, 0)]*(max_n+1)
v_lst = [[0 for i in range(max_w+1)] for j in range(max_n+1)]

for i in range(1, max_n+1):
    item_lst[i] = tuple(map(int, input().split(" ")))

print(item_lst)
print()

for i in range(1, max_n+1):
    w, v = item_lst[i]
    for j in range(max_w+1):
        if j < w:
            v_lst[i][j] = v_lst[i-1][j]
        else:
            v_lst[i][j] = max(v_lst[i-1][j], v_lst[i-1][j-w]+v)

    print(w, v)
    for l in range(len(v_lst)):
        print(v_lst[l])
    print()

print(v_lst)
