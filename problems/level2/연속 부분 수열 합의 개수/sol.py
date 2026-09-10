elements = [7, 9, 1, 1, 4]
m = len(elements)
rset = set()

for i in range(m):
    for j in range(i, m):
        rset.add(sum(elements[k] for k in range(i, j)))
        rset.add(sum(elements[0:i] + elements[j+1:]))

print(list(rset -{0}))

