t = ["3141592", "500220839878", "10203"]
p = ["271", "7", "15"]

i = 1
t = t[i]
p = p[i]

result = 0
length = len(p)
부분문자열 = [t[i:i+length] for i in range(len(t)-length+1)]
print(부분문자열)
for 문자열 in 부분문자열:
    if int(문자열) <= int(p):
        result += 1

print(result)

def solution(t, p):
    result = 0
    length = len(p)
    partial = [t[i:i+length] for i in range(len(t)-length+1)]
    for number in partial:
        if int(number) <= int(p):
            result += 1
    return result