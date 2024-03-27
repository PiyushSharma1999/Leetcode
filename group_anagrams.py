from collections import defaultdict

strs = ["eat","tea","tan","ate","nat","bat"]


def groupAnagrams(strs):
    res = {} #defaultdict(list)
    for s in strs:
        count = [0] * 26

        for c in s:
            count[ord(c) - ord("a")] += 1

        res[tuple(count)].append(s)
    
    return res.values(), res.items()
        
    

res, res1 = groupAnagrams(strs)

print(res)
print("\n")
print(res1)

# [((1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0), ['eat', 'tea', 'ate']), 
#  ((1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0), ['tan', 'nat']), 
#  ((1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0), ['bat'])]
