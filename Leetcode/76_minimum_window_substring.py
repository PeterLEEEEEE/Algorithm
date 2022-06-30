from collections import Counter

t = 'ABC'
s = "ADOBECODEBANC"
missing = len(t)
t_map = Counter(t)
left, start, end = 0, 0, 0

for right, v in enumerate(s, 1):
    missing -= t_map[v] > 0
    t_map[v] -= 1
    print(missing, t_map)
    # if t_map[v] > 0:
    #     missing -= 1
    #     t_map[v] -= 1

    if missing == 0:
        while left < right and t_map[s[left]] < 0:
            t_map[s[left]] += 1
            left += 1

        if not end or right - left <= end - start:
            start, end = left, right
            t_map[s[left]] += 1
            missing += 1
            left += 1
            
        print(s[start:end])