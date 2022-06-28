from itertools import permutations, combinations
from collections import defaultdict

s = [278, 576, 496, 727, 410, 124, 338, 149, 209, 702, 282, 718, 771, 575, 436]
k = 7
ans = set()
for i in combinations(s, 2):
    a, b = list(i)
    temp = a + b
    
    if temp % k != 0:
        ans.add(a)
        ans.add(b)

dists = defaultdict(lambda: -1)
dists[1] = 0
print(dists[2])
print(len(ans))
