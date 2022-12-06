###
### 1213번: 팰린드롬 만들기
###

import sys
input = sys.stdin.readline

# 입력값 받기
### sys.stdin.readline()은 끝에 개행문자가 들어있는데요,
### strip() 함수를 이용해 개행 문자를 지워줬습니다 ~
name = input().strip()

# 이름에 사용된 알파벳 개수 세기
alpha = [0 for _ in range(26)]
for i in range(len(name)):
    ### ord(c): char to int
    alpha[ord(name[i]) - ord('A')] += 1

# 홀수개인 문자의 개수를 세어줄 변수
odd_cnt = 0
temp = ""
center = ""
for i in range(len(alpha)):
    cnt = alpha[i]
    # 홀수개인 문자는 center에 넣어줌
    if cnt % 2:
        odd_cnt += 1
        center += chr(i + ord('A'))
    # 2개 이상인 문자는 개수의 반절만큼 temp에 넣어줌
    for _ in range(cnt // 2):
        ### chr(i): int to char
        temp += chr(i + ord('A'))

if odd_cnt > 1: # 🙏🏻
    print("I'm Sorry Hansoo")
else:
    ### [a:b:c] => a부터 b까지 c의 간격으로 배열을 만들어라 !
    ### 만약 문자의 끝이면 a, b 생략 가능, c가 생략되면 한칸 한격이라는 뜻
    ### temp[::-1] == temp을 역순으로 만듦
    print(temp + center + temp[::-1])