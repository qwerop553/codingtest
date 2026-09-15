n = 5
result = [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]

better = [set() for _ in range(n+1)]
weaker = [set() for _ in range(n+1)]

for a, b in result:
    weaker[a].add(b)
    better[b].add(a)
    for i in range(1, n+1):
        if a in weaker[i]: # i가 선수 a를 이겼기 때문에, a보다 약한 선수들은 모두 a보다 약함
            weaker[i].update(weaker[a]) # weaker[a]에 i는 없음

        if a in better[i]: # i가 선수 a에게 졌었기 때문에, a보다 강한 선수들은 모두 i보다 강함
            better[i].update(better[a])
        
        if b in better[i]: # i가 선수 b에게 졌기 때문에, b보다 강한 선수들은 모두 i보다 강함
            better[i].update(better[b]) # better[b]에 i는 없음

        if b in weaker[i]: #i가 선수 b에게 이겼었기 때문에, b보다 약한 선수들은 모두 i보다 약함
            weaker[i].update(weaker[b])
        
ans = 0
for i in range(1, n+1):
    if len(better[i]) + len(weaker[i]) == n-1:
        ans += 1

print(better)
print(weaker)
print(ans)

def solution(n, results):
    better = [set() for _ in range(n+1)]
    weaker = [set() for _ in range(n+1)]

    for a, b in result:
        weaker[a].add(b)
        better[b].add(a)
        for i in range(1, n+1):
            if a in weaker[i]: # i가 선수 a를 이겼기 때문에, a보다 약한 선수들은 모두 a보다 약함
                weaker[i].update(weaker[a]) # weaker[a]에 i는 없음

            if a in better[i]: # i가 선수 a에게 졌었기 때문에, a보다 강한 선수들은 모두 i보다 강함
                better[i].update(better[a])
            
            if b in better[i]: # i가 선수 b에게 졌기 때문에, b보다 강한 선수들은 모두 i보다 강함
                better[i].update(better[b]) # better[b]에 i는 없음

            if b in weaker[i]: #i가 선수 b에게 이겼었기 때문에, b보다 약한 선수들은 모두 i보다 약함
                weaker[i].update(weaker[b])
            
    ans = 0
    for i in range(1, n+1):
        if len(better[i]) + len(weaker[i]) == n-1:
            ans += 1

    return ans