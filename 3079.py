###
### 3079번: 입국심사
###

import sys
input = sys.stdin.readline

# 입력값 받기
n, m = map(int, input().split())
time = []
for _ in range(n):
    time.append(int(input()))

# 범위: 최소시간 ~ 최대시간 x 사람수 
start = min(time)
end = max(time) * m

# 이분 탐색
while start <= end:
    # 중간값 찾기
    mid = (start + end) // 2

    # mid 시간 동안 심사받을 수 있는 사람 수 구하기
    sum = 0
    for t in time: 
        sum += mid // t
        # 🌟 더하는 중 m을 넘으면 break -> 시간 단축 ! 🌟
        if sum > m:
            break

    # 모두 심사를 받을 수 있으면 시간 줄여보기
    if sum >= m:
        end = mid - 1
    # 모두 심사를 받을 수 없으면 시간 늘려보기
    else:
        start = mid + 1
    
print(start)