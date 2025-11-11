class Solution:
    def climbStairs(self, n: int) -> int:
        print("for example n=5 here is a visual diagram of the ways to climb the stairs" \
        "" \
        "")
        
        a = 1 
        b = 1

        for i in range (n-1): 
            temp = a
            a = a+b
            b = temp
        return a
    
# Example usage:
sol = Solution()
print(sol.climbStairs(5))  # Output: 8
# The function climbStairs calculates the number of distinct ways to climb to the top of a staircase with n steps.
# Each time you can either climb 1 or 2 steps.  The solution uses a dynamic programming approach with O(1) space complexity.
# The time complexity is O(n) since we iterate through the number of steps once. 

