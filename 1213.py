#1213 팰린드롬 만들기
import sys
input = sys.stdin.readline

word = list(map(str, input().strip()))
word_cnt = [0] * 26
for letter in word:
	word_cnt[ord(letter) - 65] += 1

odd = 0
odd_alpha = ''
left = ''
for i in range(26):
	if word_cnt[i] % 2 == 1:
		odd += 1
		odd_alpha += chr(i + 65)
	left += chr(i + 65) * (word_cnt[i] // 2)

if odd > 1:
	print("I'm Sorry Hansoo")
else:
	right = list(left)
	right.reverse()
	print(left + odd_alpha + ''.join(right))