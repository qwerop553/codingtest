fees = [180, 5000, 10, 600]
records = ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]

import math
from collections import defaultdict
def to_minutes(hhmm):
    h, m = map(int, hhmm.split(":"))
    return h * 60 + m

def fee(minutes, basic_time, basic_fee, unit_time, unit_fee):
    if minutes <= basic_time:
        return basic_fee
    return basic_fee + math.ceil((minutes - basic_time) / unit_time) * unit_fee

def solutions(fees, records):
    in_time = {}
    total = defaultdict(int)
    for record in records:
        time, car_number, car_state = record.split()
        if car_state == "IN":
            in_time[car_number] = to_minutes(time)
        else:
            total[car_number] += to_minutes(time) - in_time.pop(car_number)

    for car, t in in_time.items():
        total[car] += to_minutes("23:59") - t

    return [fee(total[car], *fees) for car in sorted(total)]

