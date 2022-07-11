# sol 3, 실패, 시간 초과
item_lst = []  # 전체 무게, 선호도 담는 2차원 리스트

def get_adds(lst):
    global max_w
    l = len(lst)
    if l > 1:
        for j in range(l - 1):
            buff = (lst[j][0] + lst[l - 1][0], lst[j][1] + lst[l - 1][1])
            if buff[0] <= max_w:
                lst.append(buff)

max_n, max_w = map(int, input().split(" "))
for i in range(max_n):
    buff = tuple(map(int, input().split(" ")))
    if buff[0] <= max_w:
        item_lst.append(buff)
        get_adds(item_lst)

item_lst = list(filter(lambda x: x[0] <= max_w, item_lst))
item_lst.sort(key=lambda x: x[1], reverse=True)
print(item_lst[0][1])