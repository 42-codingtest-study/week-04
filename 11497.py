# 통나무 건너뛰기
# https://www.acmicpc.net/problem/11497

import sys
from collections import deque	# 덱은 자료구조 중 하나임 (스택 + 큐)
								# 덱을 쓰면 양쪽으로 요소를 추가 및 삭제 할 수 있다.
								# 요소 추가 및 삭제에 대한 시간복잡도는 O(1)로 매우 효율적임 !

input = sys.stdin.readline
T = int(input())
for _ in range(T) :
    N = int(input())
    tree = list(map(int, input().split()))
    tree.sort()						# 통나무들을 정렬시켜주어 요소들을 차례로 하나씩 덱의 양쪽으로 넣어줄 것이다.
    dq = deque()					# 덱 선언
    for _ in range(N // 2) :		# 양쪽으로 넣을거라서 반만
        dq.append(tree.pop())		# 하나는 리스트처럼 오른쪽에서 넣어준다
        dq.appendleft(tree.pop())	# 다른 하나는 왼쪽으로 넣어준다
    if len(tree) == 1 :				# 두개씩 넣어줬으니까 통나무의 갯수가 홀수라면 하나가 남을것이다
        dq.append(tree.pop())		# 그러면 마지막 통나무도 넣어주면 된다
    max = abs(dq[0] - dq[-1])		# 첫 통나무와 마지막 통나무가 인접해있으므로 이 차이를 초기값으로 설정
    for i in range(N - 1) :			# 반복문을 통해 가장 최댓값을 찾아준다.
        if max < abs(dq[i] - dq[i + 1]) :
            max = abs(dq[i] - dq[i + 1])
    print(max)