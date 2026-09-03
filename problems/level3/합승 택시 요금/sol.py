# 간선에서 A까지 거리가 가장 짧을 수도 있고
# 간선에서 B까지 거리가 가장 짧을 수도 있고

# 각각 따로 가는 것보다 A와 B가 특정 구간을 공유하는 것이 더 짧을 수도 있다.
# 이걸 어떻게 코드로 구현할래?

#각 간선 간의 최소 거리를 저장하는 행렬을 만들면되는디.

n = 6; s = 4; a = 6; b = 2; fares = [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]];
adjacent_matrix = [[float('inf')] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    adjacent_matrix[i][i] = 0
for fare in fares:
    u, v, w = fare
    adjacent_matrix[u][v] = w
    adjacent_matrix[v][u] = w
    

# Floyd-Warshall 알고리즘을 사용하여 모든 쌍의 최소 거리 계산
for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            adjacent_matrix[i][j] = min(adjacent_matrix[i][j], adjacent_matrix[i][k] + adjacent_matrix[k][j])

def solution(n, s, a, b, fares):
    answer = float('inf')
    for k in range(1, n + 1):
        answer = min(answer, adjacent_matrix[s][k] + adjacent_matrix[k][a] + adjacent_matrix[k][b])
    return answer

def solution(n, s, a, b, fares):
    adjacent_matrix = [[float('inf')] * (n + 1) for _ in range(n + 1)]
    
    for i in range(1, n+1):
        adjacent_matrix[i][i] = 0
        
    for fare in fares:
        u, v, w = fare
        adjacent_matrix[u][v] = min(adjacent_matrix[u][v], w)
        adjacent_matrix[v][u] = min(adjacent_matrix[v][u], w)
    

    # Floyd-Warshall 알고리즘을 사용하여 모든 쌍의 최소 거리 계산
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                adjacent_matrix[i][j] = min(adjacent_matrix[i][j], adjacent_matrix[i][k] + adjacent_matrix[k][j])
                
    answer = float('inf')
    for k in range(1, n + 1):
        answer = min(answer, adjacent_matrix[s][k] + adjacent_matrix[k][a] + adjacent_matrix[k][b])
    return answer