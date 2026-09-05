arr = [[1,1,0,0],[1,0,0,0],[1,0,0,1],[1,1,1,1]]

def cnt(from_y, to_y, from_x, to_x):

    if from_y +1 == to_y:
        return (1, 0) if arr[from_y][from_x] == 0 else (0, 1)

    if all(arr[y][x]  == 1 for y in range(from_y, to_y) for x in range(from_x, to_x)):
        return (0, 1)

    if all(arr[y][x]  == 0 for y in range(from_y, to_y) for x in range(from_x, to_x)):
        return (1, 0)

    half = int((to_y - from_y) / 2)

    return [sum(a) for a in zip(cnt(from_y, from_y + half, from_x, from_x + half),
                                cnt(from_y, from_y + half, from_x + half, to_x),
                                cnt(from_y + half, to_y, from_x, from_x + half),
                                cnt(from_y + half, to_y, from_x + half, to_x))] 

print(cnt(0, 4, 0, 4))