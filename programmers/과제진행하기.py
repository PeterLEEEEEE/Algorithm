# 우선순위 : 새로 사작해야 하는 과제 > 멈춘 과제

def solution(plans):
    answer = []
    plans.sort(key = lambda x:x[1])
    plan_stack = []
    for l in plans:
        start_time = int(l[1].split()[0]*60) + int(l[1].split()[1])
    print()
    return answer


plans = [["science", "12:40", "50"], ["music", "12:20", "40"], ["history", "14:00", "30"], ["computer", "12:30", "100"]]
solution(plans)