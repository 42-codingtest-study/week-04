# 11399 atm문제
import sys
input = sys.stdin.readline

n = int(input())
p = list(map(int, input().split()))
p.sort() #순서대로 정렬
result = 0

for i in range(n):
	for j in range(i+1):
		result += p[j]

print(result)
