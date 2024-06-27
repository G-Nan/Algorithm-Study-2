word = input().strip().upper()

# 알파벳 빈도 계산
## 딕셔너리 만들고 1씩 추가
## 없는 것들은 새로 1 추가하기
alphabet_count = {}
for char in word:
    if char in alphabet_count:
        alphabet_count[char] += 1
    else:
        alphabet_count[char] = 1

## 최대빈도 값이랑 딕셔너리 값이랑 똑같으면 빈리스트에 붙이기
max_count = max(alphabet_count.values())
max_chars = []
for char, count in alphabet_count.items():
    if count == max_count: 
        max_chars.append(char)

# 결과 출력
if len(max_chars) > 1:
    print("?")
else:
    print(max_chars[0]) # max_chars 하면 틀림.
    ## 리스트 전체 ['Z'], 리스트 값 1개 Z
