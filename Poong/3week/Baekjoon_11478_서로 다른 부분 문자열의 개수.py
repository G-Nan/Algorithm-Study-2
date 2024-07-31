# https://www.acmicpc.net/problem/11478

import sys
input = sys.stdin.read

S = input().strip()

substrings = []


for i in range(len(S)):
    for j in range(i+1, len(S)+1):
        substrings.append(S[i:j])


substrings.sort()

# 중복 제거 및 개수 세기
unique_count = 0
prev_substring = ""
for substring in substrings:
    if substring != prev_substring:
        unique_count += 1
        prev_substring = substring


print(unique_count)
