# 팰린드롬 만들기
import sys
input = sys.stdin.readline

#입력을 받고 입력 받은 알파벳 수를 카운트
name = list(map(str, input().strip()))
name_count = [0 for i in range(26)]
answer = ''
tmp = ''
flag = 0
for i in name:
    name_count[ord(i)-65] += 1

#홀수인 경우 flag를 1 올리고 tmp에 해당 알파벳을 넣음
for i in range(26):
    if name_count[i] % 2 == 1:
        flag += 1
        tmp = chr(i+65)
    #짝수인 경우 절반에 해당하는 알파벳 넣기
    answer += chr(i+65) * (name_count[i] // 2)

reverse_answer = list(answer)
reverse_answer.reverse()
if flag > 1: #홀수인 알파벳의 갯수가 2개 이상이면 펠린드롭 불가능
    print("I'm Sorry Hansoo")
else:
    print(answer + tmp + ''.join(map(str, reverse_answer)))
    
