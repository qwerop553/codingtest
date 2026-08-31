s = 'aukks'; skip='wbqd'; index = 5; result='happy'


convert = {}
alphabet = "abcdefghijklmnopqrstuvwxyz" * 3
print(alphabet)

for i, letter in enumerate("abcdefghijklmnopqrstuvwxyz"):
    j = 0 
    for step in range(1, index+1): 
        while alphabet[i + step + j] in skip:
            j += 1
    convert[alphabet[i]] = alphabet[i + step + j]

print(''.join(convert[ss] for ss in s))
