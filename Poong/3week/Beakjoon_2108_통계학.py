# https://www.acmicpc.net/problem/2108

#N = int(input())
#numbers = [int(input()) for _ in range(N)]

import sys
input = sys.stdin.read
data = input().split()

N = int(data[0])
numbers = list(map(int, data[1:]))

# 산술평균
mean = round(sum(numbers) / N)

# 중앙값 
# N 항상 홀수여서 이걸로 ㄱㅊㅊ
sorted_numbers = sorted(numbers)
median = sorted_numbers[N // 2]

# 최빈값 계산
frequency = {}
for num in sorted_numbers:
    if num in frequency:
        frequency[num] += 1
    else:
        frequency[num] = 1

# 최빈값 리스트 만들기
max_freq = max(frequency.values())
modes = [key for key, value in frequency.items() if value == max_freq]

# 최빈값 중 두 번째 작은값 출력?
if len(modes) > 1:
    modes.sort() # 오름차순 정렬하고
    mode = modes[1] # 리스트 두번째
else:
    mode = modes[0] # 하나만 있으면 이걸로

# 범위
ranges = max(numbers) - min(numbers)

print(mean)
print(median)
print(mode)
print(ranges)


