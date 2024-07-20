N,M = map(int,input().split(' '))
K = list(map(int, input().split(' ')))

c = 0
for i in range(len(K)-1):
    for j in range(i,len(K)):
        if K[i] != K[j]:
            c += 1

print(c)