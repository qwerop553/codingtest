'''
프로그래밍보다는 그래프적 탐구가 중요했던 문제

Key Idea:
세 그래프 타입 중 두 개의 그래프 타입엔 특별한 vertex가 유일하게 존재한다.
1. 도넛 그래프에는 두 개 이상 들어오고 두 개 이상 나가는 중점.
2. 라인 그래프에는 나가는 라인이 없는, 종점에 해당하는 지점.

About Programming:
가. list의 list에 for문을 돌릴 때, 자동으로 분해되어서 받게 할 수 있다는 거. => for a, b in edges:
나. list가 iterable이므로 map함수를 이용하여 1차 int list로 변경시키고 max를 사용할 수 있다는 거 => max(map(int, double_list))
다. generated = line = eight = 0 으로 동시 초기화 하는 거
라. 변수 이름 짓기
'''


edges = [[4, 11], [1, 12], [8, 3], [12, 7], [4, 2], [7, 11], [4, 8], [9, 6], [10, 11], [6, 10], [3, 5], [11, 1], [5, 3], [11, 9], [3, 8]]

N = max(map(max, edges))
indeg = [0] * (N + 1)
outdeg = [0] * (N + 1)

for a, b in edges:
    outdeg[a] += 1
    indeg[b] += 1

generated = line = eight = 0
for v in range(1, N+1):
    if outdeg[v] >= 2 and indeg[v] == 0:
        generated = v
    if outdeg[v] == 0 and indeg[v] > 0:
        line += 1
    if outdeg[v] == 2 and indeg[v] >= 2:
        eight += 1
donut = outdeg[generated] - line - eight

print([generated, donut, line, eight])





