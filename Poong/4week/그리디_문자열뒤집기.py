import sys
input = sys.stdin.read

# 입력 받기
data = input().strip()

count0 = 0  # 전부 0으으로
count1 = 0  # 전부 1로 

if data[0] == '1':
    count0 += 1
else:
    count1 += 1

for i in range(len(data) - 1):
    if data[i] != data[i + 1]:
        # 다음 수에서 1로 바뀌는 경우
        if data[i + 1] == '1':
            count0 += 1
        # 다음 수에서 0으로 바뀌는 경우
        else:
            count1 += 1


print(min(count0, count1))