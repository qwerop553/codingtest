possible = ["aya", "ye", "woo", "ma"]

def determine(word):
    last = None
    poss = True
    while poss:
        if len(word)==0:
            return 1
        poss = False
        for pos in possible:
            if word.startswith(pos):
                if pos == last:
                    return 0
                last = pos
                word = word[len(pos):]
                poss = True 
                break
    return 0

def solution(babbling):
    return sum([determine(word) for word in babbling])