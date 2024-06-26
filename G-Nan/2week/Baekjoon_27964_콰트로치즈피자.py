import sys
input = sys.stdin.readline

n = input().strip()
pizzas = input().strip().split(' ')

dict_p = {}

for pizza in pizzas:
    if pizza[-6:] == 'Cheese':
        dict_p[pizza] = dict_p.get(pizza, 0)
            
if len(dict_p.keys()) >= 4:
    print('yummy')
else:
    print('sad')