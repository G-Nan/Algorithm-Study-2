N, M = map(int, input().split())

for i in range(N):
    a = input()
    if len(a) == M:
        print(a[::-1]) # a[시작:끝:보폭]
    else:
        print('오류')