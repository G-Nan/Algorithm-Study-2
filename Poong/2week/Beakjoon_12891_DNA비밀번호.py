# 윈도우 슬라이싱 기법 활용하는 문제
s, p = map(int, input().split())
dna_string = input().strip()
required_counts = list(map(int, input().split()))

# 필요 문자 최소 개수
A, C, G, T = required_counts

# 현재 윈도우 내 문자 개수
current_counts = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
valid_password_count = 0

# 초기 윈도우 설정
for i in range(p):
    current_counts[dna_string[i]] += 1

# 유효한 비밀번호인지 확인하는 함수
def is_valid():
    return (current_counts['A'] >= A and
            current_counts['C'] >= C and
            current_counts['G'] >= G and
            current_counts['T'] >= T)

# 초기 윈도우 검사
if is_valid():
    valid_password_count += 1

# 슬라이딩 윈도우 시작
for i in range(p, s):
    start_char = dna_string[i - p]
    new_char = dna_string[i]

    # 윈도우 내 문자 개수 업데이트
    current_counts[start_char] -= 1
    current_counts[new_char] += 1

    # 새 윈도우가 유효한지 검사
    if is_valid():
        valid_password_count += 1


print(valid_password_count)
