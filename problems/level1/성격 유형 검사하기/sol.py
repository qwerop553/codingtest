survey = [["AN", "CF", "MJ", "RT", "NA"], ["TR", "RT", "TR"]]
choices = [[5, 3, 2, 7, 5]	, [7, 1, 3]]

i = 1; survey = survey[i]; choices = choices[i]

type_score = {'R': 0, 'T': 0, 'C': 0, 'F': 0, 'J': 0, 'M': 0, 'A': 0, 'N': 0}

for i, surv in enumerate(survey):
    match choices[i]:
        case 1:
            type_score[surv[0]] = type_score[surv[0]] + 3
        case 2:
            type_score[surv[0]] = type_score[surv[0]] + 2 if surv[0] in type_score else 2
        case 3:
            type_score[surv[0]] = type_score[surv[0]] + 1 if surv[0] in type_score else 1
        
        case 5:
            type_score[surv[1]] = type_score[surv[1]] + 1 if surv[1] in type_score else 1
        case 6:
            type_score[surv[1]] = type_score[surv[1]] + 2 if surv[1] in type_score else 2
        case 7:
            type_score[surv[1]] = type_score[surv[1]] + 3 if surv[1] in type_score else 3

answer = ''
answer += 'R' if type_score['R'] >= type_score['T'] else 'T'
answer += 'C' if type_score['C'] >= type_score['F'] else 'F'
answer += 'J' if type_score['J'] >= type_score['M'] else 'M'
answer += 'A' if type_score['A'] >= type_score['N'] else 'N'
print(answer)

def solution(survey, choices):

    type_score = {'R': 0, 'T': 0, 'C': 0, 'F': 0, 'J': 0, 'M': 0, 'A': 0, 'N': 0}

    for i, surv in enumerate(survey):
        match choices[i]:
            case 1:
                type_score[surv[0]] = type_score[surv[0]] + 3
            case 2:
                type_score[surv[0]] = type_score[surv[0]] + 2 if surv[0] in type_score else 2
            case 3:
                type_score[surv[0]] = type_score[surv[0]] + 1 if surv[0] in type_score else 1
            
            case 5:
                type_score[surv[1]] = type_score[surv[1]] + 1 if surv[1] in type_score else 1
            case 6:
                type_score[surv[1]] = type_score[surv[1]] + 2 if surv[1] in type_score else 2
            case 7:
                type_score[surv[1]] = type_score[surv[1]] + 3 if surv[1] in type_score else 3

    answer = ''
    answer += 'R' if type_score['R'] >= type_score['T'] else 'T'
    answer += 'C' if type_score['C'] >= type_score['F'] else 'F'
    answer += 'J' if type_score['J'] >= type_score['M'] else 'M'
    answer += 'A' if type_score['A'] >= type_score['N'] else 'N'
    return answer