
from typing import List
from pyparsing import nums
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        freq = [[] for i in range(len(nums) + 1)]
        for n in nums:
            hashmap[n] = 1 + hashmap.get(n, 0) 
        for n, count in hashmap.items():
            freq[count].append(n)
            res = []
        for i in range(len(freq) - 1, 0, -1):   
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
                
                # I have used bucket sort to solve this problem. First I created a hashmap to store the frequency of each number in the input list. 
                # Then I created a list of lists (buckets) where the index represents the frequency and each bucket contains the numbers with that frequency. 
                # Finally, I iterated through the buckets in reverse order to collect the top k frequent elements.
                #