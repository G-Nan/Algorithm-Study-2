# Get input as a list
n1 = list(input())
n2 = list(input())

def telephone(n1, n2):
    
    a = []
    b = []
    
    # O(n)
    for i in range(len(n2)):

        # Sum of numbers in the same position
        a.append(int(n1[i]) + int(n2[i]))
        
        if i+1 == len(n1):
            continue
            
        # Sum of numbers by shifting off by one space
        b.append(int(n1[i+1]) + int(n2[i]))
        
    return a, b

# Recursive functions
while True:
    n1, n2 = telephone(n1, n2)
    if len(n1) == 1:
        break
    
# Get Tens'digit and Unit digit
td = str(n1[0])[-1]
ud = str(n2[0])[-1]

print(td + ud)