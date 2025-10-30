#my solution:
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        maps = {}
        for i, n in enumerate(nums):
            maps[n] = i  
        if target in maps:
            return maps[target]
        return -1
#optimal solution:
