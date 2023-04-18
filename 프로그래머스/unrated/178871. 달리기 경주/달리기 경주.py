def solution(players, callings):
    answer = []
    player_dict = {rank : player for rank, player in enumerate(players)}
    rank_dict = {player : rank for rank, player in enumerate(players)}
    
    # print(player_dict) # {0: 'mumu', 1: 'soe', 2: 'poe', 3: 'kai', 4: 'mine'}
    # print(rank_dict) # {'mumu': 0, 'soe': 1, 'poe': 2, 'kai': 3, 'mine': 4}

    for player in callings:
        idx = rank_dict[player] # 3
        if idx == 0: 
            continue
        prevIdx = idx - 1
        
        curName = player_dict[idx]
        prevName = player_dict[prevIdx]
        
        # pre = player_dict[prevIdx] # poe
        rank_dict[curName] = prevIdx
        rank_dict[prevName] = idx
        
        player_dict[idx] = prevName
        player_dict[prevIdx] = curName
        

        
    
    
    return list(player_dict.values())