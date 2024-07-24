# https://www.acmicpc.net/problem/13706


import sys
import math

input = sys.stdin.read
N = int(input().strip())

sqrt_N = math.isqrt(N)

print(sqrt_N)



## 찾아본방식
# import sys
# input = sys.stdin.read


# N = int(input().strip())
#  이진 탐색을 이용한 제곱근 계산
# low, high = 0, N
# while low <= high:
#     mid = (low + high) // 2
#     if mid * mid == N:
#         sqrt_N = mid
#         break
#     elif mid * mid < N:
#         low = mid + 1
#     else:
#         high = mid - 1
# else:
#     sqrt_N = high

# print(sqrt_N)
