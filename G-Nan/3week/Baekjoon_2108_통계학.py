import sys
input = sys.stdin.readline

mean_v = 0
list_i = []
dic_v = {}
max_v = -4000
min_v = 4000

n = int(input().rstrip())

for _ in range(n):
    num = int(input().rstrip())
    mean_v += num
    list_i.append(num)
    dic_v[num] = dic_v.get(num, 0) + 1
    if num > max_v:
        max_v = num
    if num < min_v:
        min_v = num

list_mode = sorted(dic_v.items(), key = lambda x:(-x[1], x[0]))

mean_v = int(round(mean_v/n, 0))
median_v = sorted(list_i)[int(n/2)]
if len(list_mode) > 1:
    if list_mode[0][1] == list_mode[1][1]:
        mode_v = list_mode[1][0]
    else:
        mode_v = list_mode[0][0]
else:
        mode_v = list_mode[0][0]
range_v = max_v - min_v

print(mean_v)
print(median_v)
print(mode_v)
print(range_v)