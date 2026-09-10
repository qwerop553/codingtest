k = 5;  ranges = [[0,0],[0,-1],[2,-3],[3,-3]]

trace = [k]; area = [0];
while (k != 1):
    if k % 2 == 0:
        area.append(area[-1] + k/2+k/4)
        k = k // 2
        trace.append(k)
        
    else:
        area.append(area[-1] + k/2+(3*k+1)/2)
        k = 3 * k + 1
        trace.append(k)

k = trace[0]
result = []
for a, b in ranges:
    if a==0 and b==0:
        result.append(area[-1])
    elif a > k + b:
        result.append(-1)
    else:
        result.append(area[k+b]-area[a])

print(result)

def solution(k, ranges):
    trace = [k]; area = [0];
    while (k != 1):
        if k % 2 == 0:
            area.append(area[-1] + k/2+k/4)
            k = k // 2
            trace.append(k)
            
        else:
            area.append(area[-1] + k/2+(3*k+1)/2)
            k = 3 * k + 1
            trace.append(k)

    k = len(trace)-1
    result = []
    for a, b in ranges:
        if a==0 and b==0:
            result.append(area[-1])
        elif a > k + b:
            result.append(-1)
        else:
            result.append(area[k+b]-area[a])

    return result

