a = list(map(int, input()))
b = list(map(str, input().split(' ')))

c = []
while True:
    for i in b:
        d = 'Cheese'
        if d == i[-6:]:
            c.append(i)
        else:
            continue
    c = set(c)
    if len(c) >= 4:
        print('yummy')
        break
    else:
        print('sad')
        break





