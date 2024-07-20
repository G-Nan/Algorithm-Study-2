a = map(int, input())
b = list(map(int,input().split(' ')))

b.sort()

c = 1
for i in b:
    if c < i:
        break
    else:
        c += i

print(c)