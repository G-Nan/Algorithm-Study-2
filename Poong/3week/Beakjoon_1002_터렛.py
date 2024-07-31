# https://www.acmicpc.net/problem/1002
import sys
input = sys.stdin.read
data = input().strip().split()

T = int(data[0])
index = 1

results = []

for _ in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, data[index:index+6])
    index += 6

    dist_sq = (x1 - x2)**2 + (y1 - y2)**2
    r1_plus_r2_sq = (r1 + r2)**2
    r1_minus_r2_sq = (r1 - r2)**2

    if dist_sq == 0:
        if r1 == r2:
            results.append(-1)  # 무한대
        else:
            results.append(0)  # 만나지 않음
    else:
        if dist_sq > r1_plus_r2_sq or dist_sq < r1_minus_r2_sq:
            results.append(0)  # 만나지 않음
        elif dist_sq == r1_plus_r2_sq or dist_sq == r1_minus_r2_sq:
            results.append(1)  # 한 점에서 만남
        else:
            results.append(2)  # 두 점에서 만남

for result in results:
    print(result)