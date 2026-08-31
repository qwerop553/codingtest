from collections import Counter

xs = ["100", "100", "100", "12321", "5525"]
ys = ["2345", "203045", "123450", "42531", "1255"]

i = 1;x = xs[i]; y= ys[i];


temp = []
X = Counter(x)
Y = Counter(y)

for num, count in X.items():
    print(f"num: {num}, count: {count}")
    print(Y.keys())
    if num in Y.keys():
        print("hi")
        print(num)
        temp.append((num, min(Counter(x)[num], Counter(y)[num])))
temp.sort(reverse=True)
answer = ''
print(temp)
for number, count in temp:
    answer += number * count
if answer == '': answer = '-1'
print(int(answer))

from collections import Counter
def solution(X, Y):
    temp = []
    x = Counter(X)
    y = Counter(Y)
    for num, count in x.items():
        if num in y.keys():
            temp.append((num, min(x[num], y[num])))
    temp.sort(reverse=True)

    answer = ''
    for number, count in temp:
        answer += number * count
    if len(temp) == 0:
        return '-1'
    if temp[0][0] =='0':
        answer = '0'
    
    return answer