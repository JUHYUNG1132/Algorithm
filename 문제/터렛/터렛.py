
N = int(input())
for i in range(N):
    x1, y1, x2, y2, r1, r2 = map(int, input().split(" "))
    len = ((x1-x2)**2 + (y1-y2)**2)**0.5
    print(f'len = {len}, res = ', end='')
    
    if(len==0 and r1==r2):
        print("-1")
    elif(abs(r1-r2) == len or r1+r2 == len):
        print("1")
    elif(abs(r1-r2)<len<r1+r2):
        print("2")
    else:
        print("0")