# sol 1, 성공, 30840KB, 80ms
for i in range(int(input())):
    pair = 0
    minus = 0
    inp = input()
    for j in range(len(inp)):
        if inp[j] == '(':
            pair += 1
        else:
            pair -= 1
            if pair < 0:
                minus +=1

    if not pair and not minus:
        print("YES")
    else:
        print("NO")
        