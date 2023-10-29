def time_to_min(time):
    h, m = time.split(':')
    return int(h) * 60 + int(m)

def solution(book_time):
    dic = {}
    for s, e in book_time:
        start_min = time_to_min(s)
        end_min = time_to_min(e)

        for min in range(start_min, end_min+10):
            if dic.get(min) == None:
                dic[min] = 1
            else:
                dic[min] += 1
    print(dic)
    return max(dic.values())

book_time = [["15:00", "17:00"], ["16:40", "18:20"], ["14:20", "15:20"], ["14:10", "19:20"], ["18:20", "21:20"]]

print(solution(book_time))