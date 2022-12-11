#통나무를 통통통~
import sys
input = sys.stdin.readline

T = int(input())

for i in range(T):
	N = int(input())
	tongs = list(map(int, input().split()))
	tongs.sort()
	result = 0
	for j in range(2, N):
		result = max(result,abs(tongs[j]-tongs[j-2]))
	print(result)