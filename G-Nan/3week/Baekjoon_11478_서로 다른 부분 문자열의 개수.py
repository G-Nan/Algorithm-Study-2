s = input()

len_s = len(s)
answer = 0

for i in range(len_s):
    list_s = []

    for j in range(len_s - i):
        alp = s[j : j + (i+1)]
        if alp in list_s:
            pass
        else:
            list_s.append(alp)
            answer += 1

print(answer)