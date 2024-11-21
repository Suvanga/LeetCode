class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        a = len(nums)-1
        b = len(nums)-1
        for i in range(a):
            for j in range (b):
                if i!=j+1:
                    if target == nums[i] + nums[j+1]:
                        return(i,j+1)
            j= j+1 
        i=i+1       
                
        
