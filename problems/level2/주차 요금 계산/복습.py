'''
About Programming
가. 차가 입차 상태인 것을 처리하는 방식에서 배울 점이 있다. 입차 시간을 보관하는 dictionary를 이용하고,
    출차되었을 때 dict.pop(key)를 이용하여 출차하지 않은 차의 시간만을 보관하게 만든다.
나. 각 차마다 주차 시간인 minutes를 초기화하지 않아도 되게 collections.defaultdict를 이용하여 깔끔하게 관리하였다.
다. 차의 번호가 작은 순으로 정렬해야 하는데, for car in sorted(dict)로 key 순으로 꺼내고, 그 값을 이용하여 fees에 준다.(감탄스럽다)
라. 우아한 변수 이름 풀기 => *fees [*는 위치 인자로 풀기, **는 키워드로 풀기]
마. 저번에도 이야기했던 것 같긴 한데 time이나 시간을 다룰 때 더 간단한 방법이 있을 수 있음. 첫 트라이에 datetime 이용하려다 힘들었음.

Trivia: 생각해 보면 들어오고 나갈 때마다 주차비를 내야 하는데, 하루 중 있었던 시간 총합으로 주차비를 내네..
'''
fees = [180, 5000, 10, 600]
records = ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]

import math 
'일단 시간에 대해 비용을 계산하는 함수를 만들 생각은 잘 한 것 같음'
def fee(minutes, basic_time, basic_fee, unit_time, unit_fee):
    if minutes <= basic_time:
        return basic_fee
    return math.ceil((minutes - basic_time) / unit_time) * unit_fee + basic_fee

'이제 문자열 시간에 대해 분을 리턴하는 함수를 만들자.'
def to_minute(hhmm):
    ''' "23:50"같은 수가 들어왔을 때'''
    h, m = map(int, hhmm.split(":"))
    return h * 60 + m 

from collections import defaultdict
def solution(fees, records):
    in_time = {}
    minutes = defaultdict(int)
    for record in records:
        time, car, action = record.split()
        if action == "IN":
            in_time[car] = time
        else:
            minutes[car] += to_minute(time) - to_minute(in_time.pop(car))

    for car, t in in_time.items():
        minutes[car] += to_minute("23:59") - to_minute(t)

    return [fee(minutes[car], *fees) for car in sorted(minutes)]

print(solution(fees, records))




