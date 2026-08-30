k = [3, 4]
score = [[10, 100, 20, 150, 1, 100, 200], [0, 300, 40, 300, 20, 70, 150, 50, 500, 1000]]

i = 0; k = k[i]; score = score[i];


class ds():

    data = []

    def append(self, n: int) -> int:
        data = self.data # swallow copy
        idx = len(data)
        for i in range(len(self.data)):
            if n > self.data[i]:
                idx = i
                break

        self.data = data[:idx] + [n] + data[idx:]

        return n

    def nlargest(self, k: int) -> int:
            return self.data[k-1] if len(self.data) >= k else self.data[len(self.data)-1]


def solution(k, score):
    ret = []
    a = ds()
    for sc in score:
        a.append(sc)
        ret.append(a.nlargest(k))
    return ret

print(solution(k, score))
