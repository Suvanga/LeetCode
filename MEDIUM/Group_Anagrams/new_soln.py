from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        res = []

        for s in strs:
            sort = tuple(sorted(s)) #changing it to tuple because keys have to immiutale
            anagrams[sort].append(s) #grouping anagrams together
        
        print (anagrams)
        for alu in anagrams.values():
            res.append(alu)
        return res
