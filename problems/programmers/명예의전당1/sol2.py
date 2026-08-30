k = [3, 4]
score = [[10, 100, 20, 150, 1, 100, 200], [0, 300, 40, 300, 20, 70, 150, 50, 500, 1000]]

i = 0; k = k[i]; score = score[i];


def solution(k, score):
    ret = []
    temp = []
    for sc in score:
        idx = len(temp)
        if idx == 0:
            temp.append(sc)
            ret.append(sc)
            continue

        for i in range(len(temp)):
            if sc > temp[i]:
                idx = i
                break

        temp = temp[:idx] + [sc] + temp[idx:] 
        ret.append(temp[min(k, len(temp))-1])
    return ret

print(solution(k, score))
