# Get input
word = input().upper()

# Count the number of characters in a word
dic_s = {}

# O(n)
for i in word:
    dic_s[i] = dic_s.get(i, 0) + 1
    
# Sort by count in descending order
# O(nlogn)
dic_s_sort = dict(sorted(dic_s.items(), key = lambda x: x[1], reverse = True))

list_val = list(dic_s_sort.values())
list_key = list(dic_s_sort.keys())

# If only one character exists, ouput that character
if len(list_val) == 1:
    print(list_key[0])

    # Compares the two characters with the highest counts
else:
    # Output ? if they are equal
    if list_val[0] == list_val[1]:
        print('?')
    # Output the first character if they are unequal
    else:
        print(list_key[0])