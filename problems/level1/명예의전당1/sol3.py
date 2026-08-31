import heapq

def solution(k, score):
    max_heap = []
    answer = []

    for sc in score:
        heapq.heappush(max_heap, sc)
        answer.append(min(heapq.nlargest(3, max_heap)))

    return answer

# 코딩테스트 시 자료구조 이용 가능하면, 이렇게 푸는 게 가장 좋지.

k = [3, 4]
score = [[10, 100, 20, 150, 1, 100, 200], [0, 300, 40, 300, 20, 70, 150, 50, 500, 1000]]

i = 0; k = k[i]; score = score[i];
solution(k, score)