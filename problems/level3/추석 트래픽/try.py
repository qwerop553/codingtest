lines = ["2016-09-15 20:59:57.421 0.351s", "2016-09-15 20:59:58.233 1.181s", "2016-09-15 20:59:58.299 0.8s", "2016-09-15 20:59:58.688 1.041s", "2016-09-15 20:59:59.591 1.412s", "2016-09-15 21:00:00.464 1.466s", "2016-09-15 21:00:00.741 1.581s", "2016-09-15 21:00:00.748 2.31s", "2016-09-15 21:00:00.966 0.381s", "2016-09-15 21:00:02.066 2.62s"]


def to_ms(hms: str):
    h, m, s = hms.split(":")
    return round(float(s) * 1000) + 1000 * (60 * int(m) + 3600 * int(h))

def elapsed_ms(elp: str):
    etime = elp.replace("s", "")
    etime = round(float(etime) * 1000)
    return etime

transactions = []
for line in lines:
    transaction = []
    _, time, elapsed = line.split()
    e = to_ms(time)
    s = e - elapsed_ms(elapsed) + 1
    transactions.append((s, e))

ans = 0
for _, end in transactions:
    w_start, w_end = end, end+999
    peak = sum(1 for s, e in transactions if w_start <= e and s <= w_end)
    ans = max(ans, peak)

print(ans)