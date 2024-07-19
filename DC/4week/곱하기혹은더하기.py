a = input()

b = []

for i in a:
    b.append(int(i))

b.sort()

c = 0
for j in b:
    if j < 2:
        c += j
    else:
        c = c*j

print(c)