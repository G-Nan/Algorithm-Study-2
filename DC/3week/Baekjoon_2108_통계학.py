import sys
from collections import Counter
n = int(sys.stdin.readline())
b = []
for _ in range(n):
    b.append(int(sys.stdin.readline()))

print(round(sum(b) / n))

b.sort()
print(b[n//2])

cnt = Counter(b).most_common()
if len(cnt) > 1 and cnt[0][1]==cnt[1][1]: 
    print(cnt[1][0])
else:
    print(cnt[0][0])
    
print(b[-1] - b[0])