#통나무 건너뛰기
import sys

input = sys.stdin.readline
t = int(input())
for i in range(t):
    n = int(input())
    data = list(map(int,input().split()))
    data.sort()
    answer = 0 
    for i in range(2,n):
        answer = max(answer, abs(data[i] - data[i-2]))
    print(answer)