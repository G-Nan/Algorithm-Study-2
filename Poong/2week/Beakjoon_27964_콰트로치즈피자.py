
n = int(input())
toppings = input().split()

# 'Cheese'로 끝나는 토핑 필터링
cheese_toppings = []
for topping in toppings:
    if topping[-6:] == 'Cheese':
        if topping not in cheese_toppings: # 없는 경우에만 추가 
            cheese_toppings.append(topping)

# 서로 다른 치즈의 개수를 확인
unique_cheese_count = len(cheese_toppings)


if unique_cheese_count >= 4:
    print("yummy")
else:
    print("sad")
