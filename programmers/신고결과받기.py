def solution(id_list, report, k):
    answer = []
    name_cnt = dict()
    temp_dict = dict()
    for name in id_list:
        name_cnt[name] = 0

    for r in report:
        reporter, reported = r.split()
        temp_dict[reported] = temp_dict.get(reported, []) + [reporter]
    
    for item in temp_dict.values():
        set_item = set(item)
        if len(set_item) >= k:
            for i in set_item:
                name_cnt[i] += 1
            
    
    print(name_cnt.values())
    return answer



id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
k = 2

result = solution(id_list, report, k)