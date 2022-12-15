# 입국심사
# https://www.acmicpc.net/problem/3079


import sys

input = sys.stdin.readline				# 입력값이 많이 들어옴
N, M = map(int, input().split())
T = [int(input()) for _ in range(N)]
left = min(T)							# 이분탐색 세팅
answer = right = max(T) * M				# 이분탐색 및 정답 세팅
while left <= right:					# 조건
    total = 0							# 입국 할 수 있는 사람 수
    mid = (left + right) // 2			# 중간 값
    for i in range(N):
        total += mid // T[i]			# 중간 값 동안 각 심사대가 받을 수 있는 사람 수
    if total >= M:						# 각 심사대가 받을 수 있는 총 사람 수가 M보다 크거나 같다면
        right = mid - 1					# right 값 설정
        answer = min(answer, mid)		# 정답 값 다시 세팅
    else:								# 긱 심사대가 받을 수 있는 총 사람 수가 M보다 작다면
        left = mid + 1					# left 값 설정
print(answer)