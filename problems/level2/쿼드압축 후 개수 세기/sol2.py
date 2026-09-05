def solution(arr):
    def cnt(y, x, n):
        vals = {arr[i][j] for i in range(y, y+n) for j in range(x, x+n)}
        if len(vals) == 1:
            return (1, 0) if vals.pop() == 0 else (0, 1)
        h = n // 2
        return tuple(map(sum, zip(*(cnt(y + dy, x + dx, h)
                                    for dy in (0, h) for dx in (0, h)))))

    return list(cnt(0, 0, len(arr)))