from bisect import bisect_right

ranked = [100, 100, 50, 40, 40, 20 , 10]
player = [5, 25, 50, 120]
answer =[]
set_rank = sorted(set(ranked))
for score in player:
    answer.append(len(set_rank)-bisect_right(set_rank, score)+1)
    
print(answer)