today = ["2022.05.19", "2020.01.01"]
terms = [["A 6", "B 12", "C 3"], ["Z 3", "D 5"]]
privacies = [["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"], ["2019.01.01 D", "2019.11.15 Z", "2019.08.02 D", "2019.07.01 D", "2018.12.28 Z"]]
result = [[1, 3], [1, 4, 5]]

i = 0
today = today[i]
terms = terms[i]
privacies = privacies[i]
result = result[i]


class Date():
    def __init__(self, st):
        self.st = st
        self.year, self.month, self.date = map(int, st.split("."))

    def __ge__(self, other):
        if self.st >= other.st:
            return True
        else:
            return False
    def __str__(self):
        return f"st: {self.st}"

    def _st_update(self):
        month = f"0{self.month}" if self.month < 10 else self.month
        date = f"0{self.date}" if self.date < 10 else self.date
        self.st = f"{self.year}.{month}.{date}"

    def add_month(self, month):
        month = int(month)
        if self.month + month > 12:
            self.month = (self.month + month) % 12
            self.year = self.year + 1
        else:
            self.month = self.month + month 
        self._st_update()
        return self

print(Date(today).st)
print(Date(today))
print(Date(today).add_month(5).st)
print(Date(today).add_month(13).st)
today = Date(today)
dic = {k: int(v) for term in terms for k, v in [term.split()]}
priv = {Date(k): v for privacy in privacies for k, v in [privacy.split(" ")]}
print(priv)
ret = []
for i, trm in enumerate(priv.items()):
    if trm[0].add_month(dic[trm[1]]) <= today:
        ret.append(i+1)

print(ret)