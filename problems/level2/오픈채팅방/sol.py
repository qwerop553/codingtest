def solution(record):
    id = {}
    events = []
    for rec in record:
        if len(rec.split()) == 2:
            cmd, uid = rec.split()
            events.append(("Leave", uid))
            continue
            
        cmd, uid, nickname = rec.split()
        if cmd == "Change":
            id[uid] = nickname
            
        else:
            events.append(("Enter", uid))
            id[uid] = nickname
    
    ans = []
    for event in events:
        if event[0] == "Enter":
            ans.append(f"{id[event[1]]}님이 들어왔습니다.")
        else:
            ans.append(f"{id[event[1]]}님이 나갔습니다.")
            
    return ans
            
solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"])
        