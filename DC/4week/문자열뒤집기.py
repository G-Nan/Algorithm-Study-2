a = input()

c0 = 0
c1 = 0

if a[0] == '1':
    c0 += 1
else:
    c1 += 1

for i in range(len(a)-1):
    if a[i] != a[i+1]:
        if a[i+1] == '1':
            c0 += 1
        else: 
            c1 += 1