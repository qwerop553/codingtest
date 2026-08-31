k = [3, 4]	
m = [4, 3]
score = [[1, 2, 3, 1, 2, 3, 1], [4, 1, 2, 2, 4, 4, 4, 4, 1, 2, 4, 2]]

i = 0
k = k[i]; m = m[i]; score = score[i];

# Find the maximum result
number = [0] * (k+1)
for sc in score:
    number[sc] += 1

result = 0

remainder = 0
for s in range(k, 0, -1):
    result += ((remainder + number[s]) // m) * s * m
    remainder = (remainder + number[s]) % m

print(result)

