from collections import defaultdict
def group_anagrams(strs):
    anagram_map = defaultdict(list)
    res = []

    for i in strs:
        sorted_s = tuple(sorted(i))
        anagram_map[sorted_s].append(i)
        
    for val in anagram_map.values():
        res.append(val)
        
    return res


print(group_anagrams(["eat","tea","tan","ate","nat","bat"]))