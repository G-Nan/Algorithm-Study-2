eq = input()

num_p = 0
num = ''
answer = 0

n_minus = 0
for i in eq + '-':

    if i == '-':
        num_p += int(num)

        if n_minus:
            answer -= num_p
        else:
            answer += num_p

        num = ''
        num_p = 0
        n_minus += 1

    elif i == '+':
        num_p += int(num)
        num = ''

    else:
        num += i
    
print(answer)