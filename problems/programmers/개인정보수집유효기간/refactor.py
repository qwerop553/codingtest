today = ["2022.05.19", "2020.01.01"]
terms = [["A 6", "B 12", "C 3"], ["Z 3", "D 5"]]
privacies = [["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"], ["2019.01.01 D", "2019.11.15 Z", "2019.08.02 D", "2019.07.01 D", "2018.12.28 Z"]]
result = [[1, 3], [1, 4, 5]]

i = 0
today = today[i]
terms = terms[i]
privacies = privacies[i]
result = result[i]

def to_days(date: str) -> int:
    year, month, day = map(int, date.split("."))
    return (12*year + month) * 28 + day

ret = []
limit = to_days(today)
terms = {term.split(" ")[0] : int(term.split(" ")[1]) for term in terms}
for i, privacy in enumerate(privacies, start=1):
    date, term = privacy.split(" ")
    if limit >= to_days(date) + terms[term] * 28:
        ret.append(i)

print(ret)

def solution(today, terms, privacies):
    ret = []
    limit = to_days(today)
    terms = {term.split(" ")[0] : int(term.split(" ")[1]) for term in terms}
    for i, privacy in enumerate(privacies, start=1):
        date, term = privacy.split(" ")
        if limit >= to_days(date) + terms[term] * 28:
            ret.append(i)
    return ret    

def to_days(date: str) -> int:
    year, month, day = map(int, date.split("."))
    return (12*year + month) * 28 + day