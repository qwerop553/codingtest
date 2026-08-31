food = [1, 3, 4, 6]

half = ""
for i, num_food in enumerate(food):
    if i == 0:
        continue
    half += str(i) * (num_food // 2)

print(half)
answer = half + '0' + half[::-1]
print(answer)  