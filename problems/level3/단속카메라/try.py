routes = [[-20,-15], [-14,-5], [-18,-13], [-5,-3]]

covered = [False] * len(routes)
routes.sort()
j = 0

ans = 0
while True:
    a, b = routes[j]
    while routes[j][0] <= b:
        j += 1
        if j == len(routes): break
    ans += 1
    if j == len(routes): break
    
print(ans)

    

