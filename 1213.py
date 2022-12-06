# 팰린드롬 만들기
# https://www.acmicpc.net/problem/1213

from collections import Counter

palin = list(input())
palin.sort()							# 사전순으로 앞서는 것을 찾기 위해
counter = Counter(palin)				# Counter를 쓰면 요소마다 몇개씩 들어있는지 알 수 있음
odd = 0
odd_char = ''
answer = ''
for i in counter :						# 각 요소가 i에 담긴다
    if counter[i] % 2 == 1 :			# counter[i] 는 i에 담긴 요소의 갯수
        odd += 1
        odd_char = i					# 만약 요소의 갯수가 홀수라면 가운데에 문자를 출력해야하기때문에 저장
    if odd > 1 :						# 홀수가 두개 이상은 팰린드롬이 불가하다
        break
    answer += i * (counter[i] // 2)		# answer에 펠린드롬의 절반 저장

if odd > 1 :
    print("I'm Sorry Hansoo")
else :
    print(answer + odd_char + answer[::-1])