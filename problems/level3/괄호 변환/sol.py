def reverse(i): return ')' if i=='(' else '('
def solution(p):
    if p == "":
        return ""

    ordered = True if p[0] == '(' else False

    left_p, right_p = 0, 0
    for i, c in enumerate(p):
        if c == '(':
            left_p += 1
        else:
            right_p += 1

        if left_p == right_p:
            if ordered:
                return p[:i+1] + solution(p[i+1:])
            
            else: 
                return '(' + solution(p[i+1:]) +  ')' + ''.join(reverse(a) for a in p[1:i])

    raise Exception()

            

p = "()))((()"
print(solution(p))

            