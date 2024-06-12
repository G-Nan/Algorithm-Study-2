n, m = map(int, input().split(' '))

a = str()

# Reverse the input string and sum
# O(n * m)
for _ in range(n):              # O(n)
    fb = input()
    a += fb[::-1] + '\n'        # O(m)

print(a)