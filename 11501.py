#홍준이새끼! 주식하지마
import sys
input = sys.stdin.readline

test = int(input().rstrip("\n"))

for _ in range(test):
	N = int(input().rstrip("\n"))
	stock = list(map(int, input().rstrip("\n").split()))
	max = 0
	result = 0

	for i in range(len(stock)-1, -1, -1):
		if stock[i] > max:
			max = stock[i]
		else:
			result += (max - stock[i])

	print(result)