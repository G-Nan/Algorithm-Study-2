import sys
input = sys.stdin.readline

n, m = map(int, input().split())
DNA = input()
list_c = list(map(int, input().split(' ')))

answer = 0
list_DNA = ['A', 'C', 'G', 'T']

pw1 = DNA[:m]

dic_pw1 = {i : 0 for i in list_DNA}
for i in pw1:
    dic_pw1[i] += 1

w = 0
for i, j in enumerate(['A', 'C', 'G', 'T']):
    if dic_pw1[j] < list_c[i]:
        break
    else:
        w += 1

if w == 4:
    answer += 1

for i in range(m, n):

    dic_pw1[DNA[i]] += 1
    dic_pw1[DNA[i-m]] -= 1
    
    w = 0
    for i, j in enumerate(['A', 'C', 'G', 'T']):
        if dic_pw1[j] < list_c[i]:
            break
        else:
            w += 1
    
    if w == 4:
        answer += 1

print(answer)