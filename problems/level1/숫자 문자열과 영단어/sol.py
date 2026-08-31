s = "one4seveneight"

def solution(s: str):
    s = s.replace("zero", '0', -1).replace("one", '1', -1).replace("two", '2', -1).replace("three", '3', -1).replace("four", '4', -1).replace("five", '5', -1).replace("six", '6', -1).replace("seven", '7', -1).replace("eight", '8', -1).replace("nine", '9', -1)
    return s

print(solution(s))