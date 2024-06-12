# https://www.acmicpc.net/problem/11945

# 입력되는 형태가 다양할듯하다
# 마지막 뒤집는건 파이썬 문자열 슬라이싱 활용해보자. 다른 방법 있나?
# 시간복잡도? 고려해보자

## 첫풀이 36ms
# 입력 받기
n, m = map(int, input().split())  # 첫 줄에서 n과 m을 입력받음

fish_bread = []  # 붕어빵 모양을 저장할 리스트

# 다음 n줄에서 붕어빵 모양을 입력받음
for _ in range(n):
    line = input().strip()  # 한 줄의 입력을 받고 공백 제거
    fish_bread.append(line)  # 리스트에 추가

# 각 행을 뒤집기
for line in fish_bread:
    print(line[::-1])  # 각 행을 뒤집어서 출력


## 두번째 40ms
# 입력 받기
n, m = map(int, input().split())  # 첫 줄에서 n과 m을 입력받음
fish_bread = [input().strip() for _ in range(n)]  # 리스트컴프리헨션

# 각 행을 뒤집기
for line in fish_bread:
    print(line[::-1])  # 각 행을 뒤집어서 출력

## 세번째 40ms -> sys 이렇게 쓰는 게 맞나?
import sys
input = sys.stdin.read

# 입력 받기
data = input().strip().split()
n, m = int(data[0]), int(data[1])
fish_bread = data[2:]

# 각 행을 뒤집기
for line in fish_bread:
    print(line[::-1])


## 네번째 -> 슬라이싱 말고 다른거 44ms
# 입력 받기
n, m = map(int, input().split())  # 첫 줄에서 n과 m을 입력받음

fish_bread = []  # 붕어빵 모양을 저장할 리스트 초기화

# 다음 n줄에서 붕어빵 모양을 입력받음
for i in range(n):
    line = input().strip()  # 한 줄의 입력을 받고 공백 제거
    fish_bread.append(line)  # 리스트에 추가

# 각 행을 뒤집기
for line in fish_bread:
    reversed_line = ''.join(reversed(line))  # reversed 함수와 join 메소드를 사용하여 문자열 뒤집기
    print(reversed_line)  # 각 행을 뒤집어서 출력
