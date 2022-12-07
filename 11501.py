# 주식
# https://www.acmicpc.net/problem/11501

import sys

input = sys.stdin.readline		# 백만개까지 입력값이 들어올 수 있으므로
T = int(input())
for _ in range(T) :
    N = int(input())
    stock = list(map(int, input().split()))
    benefit = 0
    max = 0						# 최댓값 설정
    for i in range(N - 1, -1, -1) :	# 끝에서부터 시작
        if (stock[i] > max) :		# 만약 최댓값보다 크다면 최댓값 변경
            max = stock[i]
        else :						# 아니라면 이전 값이 최댓값보다 작으므로 이득만큼 더해줌
            benefit += max - stock[i]
    print(benefit)