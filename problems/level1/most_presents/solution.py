def solution(friends: list, gifts: list) -> int:    
    friend_mat = friend_matrix(gifts, friends)
    present_ind = present_index(given_count(friend_mat), received_count(friend_mat))
    n = len(friend_mat)

    total_present = [0 for _ in range(n)]
    for i in range(n):
        for j in range(i, n):
            if friend_mat[i][j] > friend_mat[j][i]:
                total_present[i] += 1
            elif friend_mat[i][j] < friend_mat[j][i]:
                total_present[j] += 1
            else:
                if present_ind[i] > present_ind[j]:
                    total_present[i] += 1
                elif present_ind[i] < present_ind[j]:
                    total_present[j] += 1
                else:
                    pass

    return max(total_present)
    

def friend_matrix(gifts, friend):
    mat = [[0 for _ in range(len(friends))] for _ in range(len(friends))]
    for gift in gifts:
        A, B = gift.split(' ')
        mat[friend.index(A)][friend.index(B)] += 1

    return mat

def received_count(mat):
    n = len(mat)
    return [sum(mat[j][i] for j in range(n)) for i in range(n)]

def given_count(mat):
    n = len(mat)
    return [sum(mat[i][j] for j in range(n)) for i in range(n)]

def present_index(given_mat, received_mat):
    n = len(given_mat)
    return [given_mat[i] - received_mat[i] for i in range(n)]

            
    
    

friends = ["muzi", "ryan", "frodo", "neo"]
gifts = ["muzi frodo", "muzi frodo", "ryan muzi", "ryan muzi", "ryan muzi", "frodo muzi", "frodo ryan", "neo muzi"]
    
assert friend_matrix(gifts, friends) == [[0, 0, 2, 0], [3, 0, 0, 0], [1, 1, 0, 0], [1, 0, 0, 0]]
given_mat = given_count(friend_matrix(gifts, friends)) 
assert given_mat == [2, 3, 2, 1]

received_mat = received_count(friend_matrix(gifts, friends))
assert received_mat == [5, 1, 2, 0]

present_ind = present_index(given_mat, received_mat)
assert present_ind == [-3, 2, 0, 1]

print(solution(friends, gifts))
