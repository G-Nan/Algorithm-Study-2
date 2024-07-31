import sys
input = sys.stdin.read


data = input().split() # 한번에읽고 띄어쓰기 분리
n = int(data[0])
fears = list(map(int, data[1:]))

fears.sort()

group = 0  # 그룹 수
count = 0  # 현재원

# 정렬된 공포도를 하나씩 넣으며 확인
for i in fears:
    count += 1  
    if count >= i:  # 1인 모험가 1명 ok 2인 모험가 1명 x

        group += 1
        count = 0  # 초기화


print(group)
