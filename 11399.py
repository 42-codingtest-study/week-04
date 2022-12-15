# ATM
# https://www.acmicpc.net/problem/11399

N = int(input())
lst = sorted(list(map(int, input().split())))
time = 0
for i in range(N) :
    time += sum(lst[ : i + 1])
print(time)
