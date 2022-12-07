# 가장 긴 증가하는 부분 수열2
# https://www.acmicpc.net/problem/12015

import sys

input = sys.stdin.readline
N = int(input())
A = list(map(int, input().split()))
lst = [0]									# 증가 수열을 만들어 줄 것이다.
for i in range(N) :
    if A[i] > lst[-1] :						# 리스트의 가장 끝 값보다 크다면
        lst.append(A[i])					# 증가수열로 포함
    else :									# 아니라면
        max_i = len(lst)					# 이분탐색
        min_i = 0							# 준비
        while min_i < max_i :				# 이분탐색
            mid_i = (max_i + min_i) // 2	# 한다
            if lst[mid_i] < A[i] :			# 조건은s
                min_i = mid_i + 1			# 똑같다
            else :							# 상황에 따라 
                max_i = mid_i				# 약간만 바뀐다
        lst[max_i] = A[i]					# 만약 현재 값이 증가수열의 가장 끝 값보다 작다면
											# 그 값이 위치해야할 부분에 값을 변경해준다
print(len(lst) - 1)							# 초기 값인 0을 제외하면 증가수열 완성
