#주식
import sys
input = sys.stdin.readline

t = int(input())
for i in range(t):
    n = int(input())
    data = list(map(int,input().split()))
    answer = 0 
    max_price = data[-1]
    for i in range(n-2,-1,-1):
        if data[i] > max_price: #오늘 가격이 max
            max_price = data[i]
        else:
            answer += max_price-data[i] #오늘 가격이 최대가 아니면 최대 - 지금 가격 
    print(answer)