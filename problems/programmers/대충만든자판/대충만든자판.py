import math

keymap = [["ABACD", "BCEFD"], ["AA"], ["AGZ", "BSSS"]]
targets = [["ABCD", "AABB"],	["B"], ["ASA","BGZ"]]

keymap = keymap[1]
targets = targets[1]

minimum_clicks: dict = dict()

for button in keymap:
    for i, letter in enumerate(button):
        if minimum_clicks.get(letter, -1) == -1:
            minimum_clicks[letter] = i+1
        else:
            minimum_clicks[letter] = min(i+1, minimum_clicks.get(letter))

ret = []
for target in targets:
    clicks = 0
    for letter in target:
        if minimum_clicks.get(letter, -1) != -1:
            clicks += minimum_clicks.get(letter)
        else:
            clicks = -1
            break
    ret.append(clicks)

print(ret)