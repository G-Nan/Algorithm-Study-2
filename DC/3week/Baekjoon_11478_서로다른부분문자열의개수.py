S = input()
t = set()
for i in range(len(S)):
    for j in range(i,len(S)):
        t.add(S[i:j+1])

print(len(t))