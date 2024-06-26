# 번호 두개 번갈아 배치
# 번호 겹치게 더하기 해서 둘째 자리 숫자만 남기기
# 두개의 숫자가 남을 때 까지 반복
# 십의 자리가 아니면 앞에 0을 붙임(두자리 정수로 출력)

a = list(map(int, input()))
b = list(map(int, input()))

com_num = [a[0], b[0], a[1], b[1], a[2], b[2], a[3], b[3], a[4], b[4], a[5], b[5], a[6], b[6], a[7], b[7]] # for 구문 사용하는게 더 좋을 듯

while len(com_num) > 2:
    n = []
    for i in range(len(com_num)-1):
        # range를 쓰면 안돼 고정적이기 떄문 유동적인 변화가 필요하기 때문에 / -1을 한 이유는 마지막 인덱스를 하면 아웃 오브 레인지 떠서 안돼
        s = com_num[i] + com_num[i+1]
        if s > 9:
            n.append(int(str(s)[1])) # n % 10 이 더 좋아 보이긴함
        else:
            n.append(s)
    com_num = n

print(f"{com_num[0]}{com_num[1]}")


# com_num = [] # 이렇게 번갈아하기 가능
# for i in range(len(a)):
#     com_num.append(a[i])
#     com_num.append(b[i])