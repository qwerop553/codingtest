routes = [[-20,-15], [-14,-5], [-18,-13], [-5,-3]]

def solution(routes):
    routes.sort()
    j = 0

    ans = 0
    while True:
        a, b = routes[j]
        while a <= routes[j][0] <= b:
            j += 1
            if j == len(routes): break
            a, b = min(a, routes[j][0]), min(b, routes[j][1])
            
        ans += 1
        if j == len(routes): break
    
    return ans