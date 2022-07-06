
def max_v(items, cur_w=0, cur_v=0):
    return cur_v


max_n, max_w = map(int, input().split(" "))

print(f"최대 개수: {max_n}, 최대 무게: {max_w}")

item_lst = list()           # 전체 무게, 선호도 담는 2차원 리스트

for i in range(max_n):
    item_lst.append(list(map(int, input().split(" "))))

item_lst = list(filter(lambda x: x[0] <= max_w, item_lst))
item_lst.sort(key=lambda x: x[1], reverse=True)

print(item_lst)

result = max_v(item_lst)
