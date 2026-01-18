from collections import defaultdict
from typing import List
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {defaultdict(list)}
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            res[tuple(count)].append(s)
        return list(res.values())
    

groupAnagrams = Solution().groupAnagrams

# Example usage:
sol = Solution()
if __name__ == "__main__": # we use this because the platform may run all code at import time
    input_strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(sol.groupAnagrams(input_strs))