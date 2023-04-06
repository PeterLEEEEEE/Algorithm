def solution(name, yearning, photo):
    answer = []

    dic = {}
    for i in range(len(name)):
      dic[name[i]] = yearning[i]

    for photo_names in photo:
      yearning_cnt = 0
      for name in photo_names:
        try:
          yearning_cnt += dic[name]
        except:
          pass
      answer.append(yearning_cnt)
    # return dic
    return answer

name = ["may", "kein", "kain", "radi"]
yearning = [5, 10, 1, 3]
photo = [["may", "kein", "kain", "radi"],
         ["may", "kein", "brin", "deny"],
         ["kon", "kain", "may", "coni"]]

print(solution(name, yearning, photo))