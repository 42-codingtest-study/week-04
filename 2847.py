# 게임을 만든 동준이
import sys
input = sys.stdin.readline

n = int(input())
level_lst = []
count = 0
#레벨 점수 담기
for i in range(n):
    level_lst.append(int(input()))
    
for i in range(n-1, 0, -1):
    if level_lst[i] <= level_lst[i-1]:
        count += (level_lst[i-1] - level_lst[i] + 1)
        level_lst[i-1] = level_lst[i] - 1
print(count)

    
    