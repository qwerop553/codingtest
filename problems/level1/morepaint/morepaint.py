n = 8
m = 4
section = [2, 3, 6]

# 앞에서부터 칠해도 손해보는 경우가 전혀 없다.

result = 1
wall = section[0]
section = section[1:]
for next in section:
    if next - wall < m:
        pass
    else: 
        wall = next
        result += 1

print(result)