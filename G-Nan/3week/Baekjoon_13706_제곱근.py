n = int(input().strip())

s = 1
e = n

while True:
    thr = (s + e) // 2
    if thr ** 2 == n:
        answer = thr
        break
    elif thr ** 2 > n:
        e = thr - 1
    elif thr ** 2 < n:
        s = thr + 1
print(answer)