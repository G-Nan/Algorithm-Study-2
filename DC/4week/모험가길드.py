N = map(int,input())
X = list(map(int, input().split(' ')))
X.sort()
r = 0
count = 0

for i in X:
    count += 1
    if count >= i:
        r += 1
        count = 0

print(r)
    