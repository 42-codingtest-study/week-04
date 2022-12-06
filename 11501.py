###
### 11501번: 주식
###

import sys
input = sys.stdin.readline

# 입력값 받기
t = int(input())

for _ in range(t):
    # 입력값 받기
    n = int(input())
    price = list(map(int, input().split()))

    # 역순으로 뒤집기
    price = price[::-1]
    
    profit = 0
    max = price[0]
    for i in range(1, n):
        # max보다 작으면 이익 더하기 (주식을 판다)
        if (max > price[i]):
            profit += max - price[i]
        # max 바꿔주기 (아무것도 안한다)
        else:
            max = price[i]
    print(profit)