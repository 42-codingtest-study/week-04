#2847 동준이 게임한다~
import sys
input = sys.stdin.readline

n = int(input())
score = [int(input()) for _ in range(n)]
score.reverse()
result = 0

for i in range(n-1):
	if score[i] <= score[i+1]:
		result += score[i+1] - score[i] + 1
		score[i+1] = score[i] - 1

print(result)
