'''
이건 문자열 처리네

문자열 처리 개념에 대해서 정리해 보자.
1. indexing으로 변경할 수 없다. 즉 id[b] = 'a'같은 처리는 불가능하다.
2. 대소문자를 변경하는 함수. lower()
3. 알파벳 혹은 숫자인지 검증하는 함수. isalnum (IS ALphabet or NUMber)
4. re.sub 는 정규식을 이용하여 문자를 변경할 수 있다.
5. 정규식에선 .는 어떠한 문자든 이라고 인식되어. \.처럼 백슬래시 사용해야 한다.
6. str.strip()은 항상 우리는 default로 사용했지만, 기본적으로 인자를 주게 되면 인자가 나타나지 않을 때까지 해당 값을 삭제한다.
'''

import re
id = "...!@BaT#*..y.abcdefghijklm"
id = id.lower()
id = ''.join(c for c in id if c.isalnum() or c in '-_.')
id = re.sub(r'\.+', r'\.', id)
if not id:
    id = 'a'
if len(id) >= 16:
    id = id[:16]
    if id[15] == '.':
        id = id[:15] # 마침표가 두 개 연속으로 나오는 경우는 이미 제외시켰음
while len(id) <= 2:
    id += id[-1]

print(id)

import re
def solution(new_id: str):
    new_id = new_id.lower()
    new_id = ''.join(c for c in new_id if c.isalnum() or c in '-_.')
    new_id = re.sub(r'\.+', '.', new_id)
    new_id = new_id.strip('.')
    if not new_id:
        new_id = 'a'

    if len(new_id) >= 16:
        new_id = new_id[:15]
        if new_id[-1] == '.':
            new_id = new_id[:-1]

    while len(new_id) < 3:
        new_id += new_id[-1]

    return new_id