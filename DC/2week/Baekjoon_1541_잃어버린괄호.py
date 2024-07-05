a = list(input().split('-'))

c =[]

for i in a:
    d = []
    g = i.split('+')
    for f in g:
        d.append(int(f))
    e = sum(d)
    c.append(e)

num = c[0]
for j in c[1:]:
    num -= j

print(num)


## 런타임 발생했지만 더 간단한 코드
# c =[]
# for i in a:
#     b = eval(i) 여기서 런타임 에러 발생
#     c.append(b)

# num = c[0]
# for j in c[1:]:
#     num -= j
    
# print(num)