fees = [180, 5000, 10, 600]
records = ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]

import math
def money(minutes, fees):
    basic_time = fees[0]; basic_fee = fees[1]; unit = fees[2]; multiple = fees[3];
    if minutes <= basic_time:
        return basic_fee
    else:
        return basic_fee + math.ceil((minutes - basic_time) / unit) * multiple

# def calculate(records):

timeline = sorted(records, key=lambda i: (i.split()[1], i.split()[0]))

from datetime import datetime
ans = []
minute_stayed = 0
car_is_in = False
prev_time = datetime.strptime(timeline[0].split()[0], "%H:%M")
car_number = timeline[0].split()[1]
for tl in timeline:
    # 차량이 바뀔 때 n을 초기화한다.
    if tl.split()[1] != car_number:
        if car_is_in:
            minute_stayed += (datetime.strptime("23:59", "%H:%M") - prevtime).seconds / 60
        ans.append(minute_stayed)
        minute_stayed = 0
        car_is_in = True
        car_number = tl.split()[1]
        prevtime = datetime.strptime(tl.split()[0], "%H:%M")

    
    # 차량이 변경되지 않음
    elif car_is_in:    
        minute_stayed += (datetime.strptime(tl.split()[0], "%H:%M") - prevtime).seconds / 60
        car_is_in = False
    else:
        prevtime = datetime.strptime(tl.split()[0], "%H:%M")
        car_number = tl.split()[1]
        car_is_in = True

if car_is_in:
    minute_stayed += (datetime.strptime("23:59", "%H:%M") - prevtime).seconds / 60
ans.append(minute_stayed)


print([money(an, fees) for an in ans])
   
from datetime import datetime     
def solution(fees, records):



    
