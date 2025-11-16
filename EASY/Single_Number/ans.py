from typing import List
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result =0 
        for n in nums:
            result = n^result
        return result
    
    # I am using the XOR bitwise operation to solve this problem.
    # The XOR operation has a property that a^a = 0 and a^0 = a.
    # Therefore, when we XOR all the numbers in the list, the numbers that appear twice will cancel each other out and result in 0.
    # The number that appears only once will be XORed with 0, resulting in the
    # same number. Thus, the final result will be the number that appears only once.
        # The time complexity of this solution is O(n) and the space complexity is O(1).
        #lets test this approach with an example

sol = Solution()
print(sol.singleNumber([4,1,2,1,2]))  # Expected output: 4
