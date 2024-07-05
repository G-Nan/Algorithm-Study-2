### 1
# 입력 받기
n = int(input())  
numbers = input().strip()  

# 숫자들을 더하기
total_sum = sum(int(digit) for digit in numbers)

# 결과 출력
print(total_sum)


### 2
# 입력 받기
n = int(input())  # 첫 줄에서 숫자의 개수 N을 입력받음
numbers = input().strip()  # 두 번째 줄에서 숫자들을 공백 없이 입력받음

# 숫자들을 더하기
total_sum = 0
for digit in numbers:
    total_sum += int(digit)

# 결과 출력
print(total_sum)
