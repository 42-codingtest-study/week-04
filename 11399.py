###
### 11399번: ATM
###

import sys
input = sys.stdin.readline

# 입력값 받기
n = int(input())
time = list(map(int, input().split()))

# 인출 시간이 적은 순서대로 정렬
time.sort()

sum = 0
for i in range(n):
    for j in range(n - i):
        sum += time[j]

print(sum)