id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
k = 2

reports = [repo.split(" ") for repo in report]
print(reports)

matrix = [[0] * len(id_list) for _ in range(len(id_list))]
for a, b in reports:
    matrix[id_list.index(a)][id_list.index(b)] = 1

print(matrix)

counts = [0] * len(id_list)
for i in range(len(matrix)):
    for j in range(len(matrix)):
        counts[i] += matrix[j][i]

print(counts)

mails = [0] * len(id_list)
for idx, i in enumerate(counts):
    for j in range(len(matrix)):
        if i >= k and matrix[j][idx]:
            mails[j] += 1

print(mails)

def solution(id_list, report, k):
    N = len(id_list)
    report = [repo.split(" ") for repo in report]
    matrix = [[0] * len(id_list) for _ in range(N)]
    for reporter, reported in report:
        matrix[id_list.index(reporter)][id_list.index(reported)] = 1

    n_report = [0] * N
    for i in range(N):
        for j in range(N):
            n_report[i] += matrix[j][i]

    mails = [0] * N
    for idx, i in enumerate(n_report):
        if i >= k:
            for j in range(N):
                mails[j] += 1 if matrix[j][idx] >= 1 else 0

    return mails

             
