grid = [[1, 0, -1], [0, 0, 7], [0, 0, 2]]

n, m = len(grid), len(grid[0])
CONN = {1:{'L','R'}, 2:{'U','D'}, 3:{'L','R','U','D'},
    4:{'U','L'}, 5:{'U','R'}, 6:{'D','R'}, 7:{'D','L'}}
OPP   = {'L':'R','R':'L','U':'D','D':'U'}
DELTA = {'L':(0,-1),'R':(0,1),'U':(-1,0),'D':(1,0)}
PLACE = {s:[t for t in range(1,8) if t!=3 and s in CONN[t]] for s in 'LRUD'}

cur  = [row[:] for row in grid]
used = [[set() for _ in range(m)] for _ in range(n)]   # 'h'=가로로 지나감, 'v'=세로로 지나감
ans = 0

print(PLACE)