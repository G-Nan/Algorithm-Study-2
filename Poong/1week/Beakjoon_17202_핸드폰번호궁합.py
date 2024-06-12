# 입력 받기
a = input().strip()
b = input().strip()

# 1. 두 번호를 번갈아 가면서 배열에 적기
combined = []
for x, y in zip(a, b):
    combined.append(int(x))
    combined.append(int(y))

# 2. 배열의 두 숫자를 더하여 결과 배열을 업데이트
while len(combined) > 2:
    next_combined = []
    for i in range(len(combined) - 1):
        next_combined.append((combined[i] + combined[i + 1]) % 10) # 일의 자리 숫자 남기게
    combined = next_combined

# 3. 두 숫자만 남을 때까지 반복
result = f"{combined[0]}{combined[1]}"

# 결과 출력
print(result)
