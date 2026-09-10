n = 8
queen = [[True] * n for _ in range(n)]


def plant(y, x):
    for i in range(n):
        for j in range(n):
            if i == y or j == x or abs(y-i)==abs(x-j):
                queen[i][j] = False

ans = 0
start_pos = [(0, x) for x in range(n)]
for start_y, start_x in start_pos:
    queen = [[True] * n for _ in range(n)]
    cnt = 1
    plant(start_y, start_x)
    for i in range(n):
        for j in range(n):
            if queen[i][j]:
                plant(i, j)
                cnt += 1

    if cnt == n:
        ans += 1

print(ans)

# 그냥 이렇게 넘기는 게 나을 거 같은데
[9, 2, 1, 12, 3,]
# => 1행에 9번쨰, 2행에 2번째, 3행에 1번째 배치했다...