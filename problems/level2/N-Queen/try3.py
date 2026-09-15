x = {}; y = {}; xpy = {}; xmy = {}

def queens(r, c):
    if r in y or c in x or r+c in xpy or r-c in xmy: return 0
    y[r] = True; x[c] = True; xpy[r+c] = True; xmy[r-c] = True;
    ans = sum(queens(r+1, i) for i in range(8))
    del y[r]; del x[c]; del xpy[r+c]; del xmy[r-c]
    return ans if r < 7 else 1

print(sum(queens(0, i) for i in range(8)))