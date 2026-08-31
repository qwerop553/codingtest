sizes = [[60, 50], [30, 70], [60, 30], [80, 40]]

SIZES = []
for size in sizes:
    if size[0] > size[1]:
        SIZES.append(size)
    else:
        SIZES.append([size[1], size[0]])

SIZES.sort(key=lambda i: -i[0])
x = SIZES[0][0]
SIZES.sort(key=lambda i: -i[1])
y = SIZES[0][1]
print(x*y)