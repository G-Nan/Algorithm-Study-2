import sys
input = sys.stdin.read


data = input().strip() # 한번에 읽고 공백제거

result = int(data[0]) # 첫번째 지정


for i in range(1, len(data)): # 둘째숫자부터 끝까지
    num = int(data[i])
    # 두 수 중에서 하나라도 0~1인 경우, 더하기 수행
    # 곱하는 게 무조건커짐. 0~1제외하고
    if num <= 1 or result <= 1:
        result += num
    else:
        result *= num


print(result)
