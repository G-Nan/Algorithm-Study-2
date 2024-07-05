x0 = int(input())
location = []
for i in range(x0):
    turrets = list(map(int, input().split()))
    location.append(turrets)

for t in location:
    distance = ((t[0] - t[3])**2 + (t[1] - t[4])**2)**(1/2)
    sum_r = t[2] + t[5]
    dif_r = abs(t[2] - t[5])
    
    
    if (distance == 0) and (dif_r == 0):
        answer = -1
    elif (distance > sum_r) or (distance < dif_r):
        answer = 0
    elif (distance == sum_r) or (distance == dif_r):
        answer = 1
    elif dif_r < distance < sum_r:
        answer = 2
    
    print(answer)