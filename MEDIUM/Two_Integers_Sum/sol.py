#This is my solution for the problem
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #index 1 + index 2 will have to give the target, index 1 < index 2 
        HashMap = {}
        remain =0
      
        for i, n in enumerate(numbers):
            remain = target - n
            
            if remain in HashMap:
                # return indices, 1-based
                return [HashMap[remain] + 1, i + 1]
            
            HashMap[n] = i

#this is my solution for solving the problem, as I have done a similar problem with the Two sum, This one is a medium problem