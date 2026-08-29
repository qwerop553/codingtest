bandage = [5, 1, 5]
health = 30
attacks = [[2, 10], [9, 15], [10, 5], [11, 5]]
result = 5

def solution(bandage, health, attacks):
    max_health = health
    lastTime = attacks[-1][0]
    index = 0
    conti = 0
    for time in range(1, lastTime+1):
        if attacks[index][0] == time:
            health -= attacks[index][1]
            index += 1
            conti = 0
            if health <= 0:
                return -1
        else:
            health = min(max_health, health + bandage[1])
            conti += 1
            if conti == bandage[0]:
                health = min(max_health, health + bandage[2])
                conti = 0
    return health

print(solution(bandage, health, attacks))
