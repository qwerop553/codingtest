lottos = [44, 1, 0, 0, 31, 25]
win_nums = [31, 10, 45, 1, 6, 19]

def order(correct):
    if correct <= 1:
        return 6
    return 7 - correct

def solution(lottos, win_nums):
    zeros = 0
    count = 0
    for num in lottos:
        if num == 0:
            zeros += 1
        elif num in win_nums:
            count += 1
        else:
            pass
    return [order(zeros+count), order(count)]





