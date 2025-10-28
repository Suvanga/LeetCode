from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = {} 
        for i , n in enumerate(nums):
            remain = target - n
            if remain in indices:
                return [indices[remain],i]
            indices[n] = i
# Example usage:
solve = Solution()
print(solve.twoSum([2,2,7,11,15], 9))  #