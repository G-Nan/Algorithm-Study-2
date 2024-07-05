import sys

dic_w = {}
cnt = 0
for line in sys.stdin:
    if line == '/n':
        break

    wood = line.strip()
    dic_w[wood] = dic_w.get(wood, 0) + 1
    cnt += 1
        
dic_w = dict(sorted(dic_w.items(), key = lambda x:x[0]))
for key, value in dic_w.items():
    print(key, '%.4f' %round((value/cnt) * 100, 4))