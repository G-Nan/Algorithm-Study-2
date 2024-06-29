def binary_search(a, b):
    target = b
    while True:
        mid = (a + b) // 2
        if (mid ** 2) == target:
            return mid
        if mid ** 2 > target:
            b = mid
        elif mid ** 2 < target:
            a = mid

N = int(input())
print(binary_search(1, N))

# 이분 탐색으로 푸는 방법
# N의 제곱근은 보통 1, N까지 숫자 중 하나
# 1~N까지 하나하나 탐색하기엔 시간이 오래 걸림
# 그래서 시간을 줄일 수 있는 이진 탐색으로 함
# 중앙값을 기준해서 중앙값 제곱근이 타켓인 N보다 크면 탐색 범위를 중앙값 기준 좌측으로 옮겨서 값이 작게 나올 수 있게하고 작으면 그 반대로
# 최종적으로 중앙값이의 제곱근이 타켓값과 일치 시 답이 나오게 됨  

# a = input()
# b = int(int(a)**0.5) 
# 값이 너무 클때 컴퓨터가 처리 하지 못해서 오버 플로우 에러 뜨는거 같음
# print(b) 