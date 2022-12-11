t = int(input())

for i in range(t):
    n = int(input())
    stock = list(map(int, input().split()))
    result = 0
    max = stock[-1]

    for j in range(n-2, -1, -1):
        if stock[j] > max:
            max = stock[j]
        else:
            result += max - stock[j]
    print(result)