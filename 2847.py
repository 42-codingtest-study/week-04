# 게임을 만든 동준이
# https://www.acmicpc.net/problem/2847

N = int(input())
score = [int(input()) for _ in range(N)]
answer = 0
max_score = score[N - 1]					# 가장 마지막 인덱스를 max_score로 지정
for i in range(N - 2, -1, -1) :				# 가장 마지막 인덱스는 제외
    if (max_score <= score[i]) :			# 만약 바로 이전 값이 max_score보다 높은 값이라면
        answer += score[i] - max_score + 1	# 얼마만큼 빼야하는지 answer에 추가
        score[i] = max_score - 1			# max_score - 1이 되어야 가장 최소로 점수를 감소시키는 방법
    max_score = score[i]					# 반복을 위해 max_score 다시 지정
print(answer)