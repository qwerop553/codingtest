words = ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]

def solution(n, words):
    used = {words[0]}
    for idx in range(1, len(words)):
        word = words[idx]
            
        if word in used or words[idx-1][-1] != word[0]:
            q, r = divmod(id, n)
            return [q+1, r+1]

        used.add(word)

    return [0, 0]

solution(3, words)