data = [[1, 20300104, 100, 80], [2, 20300804, 847, 37], [3, 20300401, 10, 8]]
ext = "date"
val_ext = 20300501
sort_by = "remain"


index = []
columns = ['code', 'date', 'maximum', 'remain']
for i in range(len(data)):
    if data[i][columns.index(ext)] < val_ext:
        index.append(i)

pick = sorted(index, key = lambda i: data[i][columns.index(sort_by)])
result = [data[pic] for pic in pick]
print(result)