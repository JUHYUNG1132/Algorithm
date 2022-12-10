

def find(lst: list, x: int)-> int:
    temp = x
    while(lst[x] != x):
        x = lst[x]
    lst[temp] = x
    return x

def union(lst: list, x: int, y: int)-> None:
    root_x = find(lst, x)
    root_y = find(lst, y)
    lst[root_y] = root_x
    
def is_union(lst: list, x: int, y: int)-> None:
    root_x = find(lst, x)
    root_y = find(lst, y)
    if(root_x == root_y):
        print("YES")
    else:
        print("NO")
    

n, m = map(int, input().split(" "))

lst = [i for i in range(n+1)]

for i in range(m):
    op, a, b = map(int, input().split(" "))
    
    if(op):
        is_union(lst, a, b)
    
    else:
        union(lst, a, b)
        