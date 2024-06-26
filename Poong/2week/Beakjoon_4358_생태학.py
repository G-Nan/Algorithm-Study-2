import sys

# 입력 받기
input = sys.stdin.read
data = input().strip().split('\n')

# 나무 종의 빈도를 계산하기 위한 사전 초기화
tree_count = {}
total_tree = 0

# 각 나무 종의 이름을 읽고 빈도 기록하기
for tree in data:
    if tree in tree_count: # 있으면 1증가시키기ㅣ
        tree_count[tree] += 1
    else:
        tree_count[tree] = 1 # 없으면 새로 추가 1로 설정
    total_tree += 1 # 각 종 읽을 때마다 총 카운트 

# 나무 종 이름을 사전순으로 정렬
sorted_trees = sorted(tree_count.items())
## 딕셔너리에서 items()는 키, 값 모두 출력 keys()는 키만출력
## values()는 딕셔너리 값 출력 ex.[('tree',4),('rr',3)]

# 결과 출력
for tree, count in sorted_trees: # 딕셔너리 for문 키 값 각각 들어가서
    percentage = (count / total_tree) * 100
    print(f"{tree} {percentage:.4f}") # f포멧팅 소수점4자리
