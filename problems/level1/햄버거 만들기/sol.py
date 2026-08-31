ingredient = [2, 1, 1, 2, 3, 1, 2, 3, 1]
ingredient2 = [1, 3, 2, 1, 2, 1, 3, 1, 2]

n_burger = 0
while True:
    n_ingredient = len(ingredient)
    if n_ingredient < 4:
        break
    hamburger_makable = False
    for i in range(n_ingredient - 3):
        if ingredient[i: i+4] == [1, 2, 3, 1]:
            n_burger += 1
            ingredient = ingredient[0: i] + ingredient[i+4: n_ingredient]
            hamburger_makable = True
    if not hamburger_makable: break

print(n_burger)

def solution(ingredient):
    n_burger = 0
    while True:
        n_ingredient = len(ingredient)
        if n_ingredient < 4:
            break
        hamburger_makable = False
        for i in range(n_ingredient - 3):
            if ingredient[i: i+4] == [1, 2, 3, 1]:
                n_burger += 1
                ingredient = ingredient[0: i] + ingredient[i+4: n_ingredient]
                hamburger_makable = True
                break
        if not hamburger_makable: break

    return n_burger

#아 시간 초과가~(50/100)

        
