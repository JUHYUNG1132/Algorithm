# sol 2, 통과, 메모리 226756KB, 시간 5896ms

max_n, max_w = map(int, input().split(" "))

v_lst = [[0 for i in range(max_w+1)] for j in range(max_n+1)]

for i in range(0, max_n):
    w, v = map(int, input().split(" "))
    for j in range(max_w+1):
        if j < w:
            v_lst[i][j] = v_lst[i-1][j]
        else:
            v_lst[i][j] = max(v_lst[i-1][j], v_lst[i-1][j-w]+v)

    # print(w, v)
    # for l in range(len(v_lst)):
    #     print(v_lst[l])
    # print()

print(v_lst[max_n-1][max_w])
