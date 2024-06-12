num_l = int(input())
num = input()

answer = 0

# O(n)
for i in num:
    answer += int(i)

print(answer)