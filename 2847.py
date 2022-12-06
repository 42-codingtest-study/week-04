###
### 2847번: 게임을 만든 동준이
###

import sys
input = sys.stdin.readline

# 입력값 받기
n = int(input())
score = []
for _ in range(n):
    score.append(int(input()))

cnt = 0
for i in range(1, n):
    # 낮은 난이도의 레벨 점수가 높은 난이도의 레벨 점수보다 크거나 같으면 점수 감소
    while score[n - i] <= score[n - i - 1]:
        score[n - i - 1] -= 1
        cnt += 1

print(cnt)