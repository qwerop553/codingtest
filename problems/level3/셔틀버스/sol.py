def solution(n, t, m, timetable):
    
    def time(hhmm):
        h, m = map(int, hhmm.split(":"))
        return h * 60 + m 

    def strftime(time):
        h, m = divmod(time, 60)
        return f"{h:02d}:{m:02d}"
    
    crew = [time(tbl) for tbl in sorted(timetable)]
    crew_idx = 0
    latest_time = 0

    for bus in range(time("9:00"), time("09:00")+(n-1)*t+1, t):
        i = 0
        while i < m and crew_idx < len(crew):
            latest_crew = crew[crew_idx]
            if latest_crew <= bus:
                i += 1 # 이 버스에 한 명이 추가 탑승
                crew_idx += 1
            else: # 이 크루는 버스에 탑승하지 못함
                break
        if i < m: # 승객 정원이 꽉 차지 않음. 버스 출발 시간에 도착해도 됨
            latest_time = max(bus, latest_time)
        else: # 이 버스를 타려면 마지막에 탄 크루보다 1분 빨리 오면 충분함
            latest_time = max(latest_crew-1, latest_time)

    return strftime(latest_time)