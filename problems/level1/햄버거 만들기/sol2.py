ingredient2 = [2, 1, 1, 2, 3, 1, 2, 3, 1]
ingredient = [1, 3, 2, 1, 2, 1, 3, 1, 2]

n_burger = 0
sangsoo = []
for i, ing in enumerate(ingredient):
    sangsoo.append(ing)
    if ing == 1 and len(sangsoo)>= 4:
        if sangsoo[-1]==1 and sangsoo[-2]==3 and sangsoo[-3]==2 and sangsoo[-4]==1:
            n_burger += 1;sangsoo.pop();sangsoo.pop();sangsoo.pop();sangsoo.pop();



print(n_burger)

def solution(ingredient):
    n_burger = 0
    sangsoo = []
    for i, ing in enumerate(ingredient):
        sangsoo.append(ing)
        if ing == 1 and len(sangsoo)>= 4:
            if sangsoo[-1]==1 and sangsoo[-2]==3 and sangsoo[-3]==2 and sangsoo[-4]==1:
                n_burger += 1;sangsoo.pop();sangsoo.pop();sangsoo.pop();sangsoo.pop();



    return n_burger


        
