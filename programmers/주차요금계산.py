from datetime import *

records = ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]
fees = [180, 5000, 10, 600]

def sol(fees, records):
    ans = []
    base_time, base_fee, ad_time, ad_fee = [*fees]
    
    records.sort(key=lambda x: x.split()[1])
    print(records)
    dic = {}
    i = 0
    
    while i < len(records):
        temp1 = records[i]
        if i + 1 < len(records):
            temp2 = records[i+1]
        else:
            temp2 = '0 0 0'

        if temp1.split()[1] == temp2.split()[1] and temp1.split()[2] == 'IN' and temp2.split()[2] == 'OUT':
            arrival = datetime.strptime(temp1.split()[0], '%H:%M')
            depart = datetime.strptime(temp2.split()[0], '%H:%M')
            i += 2
        else:
            auto_dep = '23:59'
            arrival = datetime.strptime(temp1.split()[0], '%H:%M')
            depart = datetime.strptime(auto_dep, '%H:%M')
            i += 1
        
        time_diff = str(depart - arrival)
        stay_time_to_min = int(time_diff.split(':')[0]) * 60 + int(time_diff.split(':')[1])
        
        # if stay_time_to_min <= base_time:
            
        dic[temp1.split()[1]]= dic.get(temp1.split()[1], 0) + stay_time_to_min
        # else:
            # over_time = stay_time_to_min - base_time
            # cnt = 0 
            # if over_time % ad_time != 0:
            #     cnt = over_time // ad_time + 1
            # else:
            #     cnt = over_time // ad_time
            
            # dic[temp1.split()[1]] = base_fee + (cnt * ad_fee)
        # dic[temp1.split()[1]] = dic.get(temp1.split()[1], 0) + (base_fee + (cnt * ad_fee))
        
    for val in dic.values():
        if val <= base_time:
            ans.append(base_fee)
        else:
            new_val = val - base_time
            if new_val % ad_time == 0:
                ans.append(base_fee + ad_fee * (new_val // ad_time))
            else:
                ans.append(base_fee + ad_fee * ((new_val // ad_time) + 1))
    return ans



ans = sol(fees, records)
print(ans)