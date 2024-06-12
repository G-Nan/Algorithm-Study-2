a = input().upper() # 시간초과ㅠㅠ

n = {}

for i in a:
    n[i] = a.count(i)

if list(n.values()).count(max(n.values())) >= 2:
    print('?')
else:
    print(max(n))


a = input().upper() # 하 결국 답지 참고함
a2 = list(set(a))
n = []

for i in a2:
    co = a.count(i)
    n.append(co)

if n.count(max(n)) >= 2:
    print('?')
else:
    print(a2[n.index(max(n))])