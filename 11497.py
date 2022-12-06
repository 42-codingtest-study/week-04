###
### 11497번: 통나무 건너뛰기
###

import sys
input = sys.stdin.readline

# 절대값 함수
def abs(a, b):
    if a > b:
        return a - b
    else:
        return b - a

# 입력값 받기
t = int(input())

for _ in range(t):
    # 입력값 받기
    n = int(input())
    length = list(map(int, input().split()))

    # 정렬
    length.sort()

    # 홀수번째 순서대로 넣어주기
    tree = []
    for i in range(0, n, 2):
        tree.append(length[i])
    # 홀수, 짝수 플래그
    flag = 1
    if n % 2:
        flag = 0
    # 짝수번째 역순으로 넣어주기
    for i in range(n - 2 + flag, 0, -2):
        tree.append(length[i])

    # 인접한 길이의 차이 중 가장 큰 값 구하기
    result = abs(tree[0], tree[n - 1])
    for i in range(1, n):
        result = max(result, abs(tree[i], tree[i - 1]))
    
    print(result)