def solution(A, B):
    A.sort()
    B.sort()
    N = len(A)
    ans = 0
    i, j = 0, 0;
    while i < N and j < N:
        if A[i] < B[j]: 
            ans += 1; i+=1; j+=1
        else:
            j+=1
        
    return ans