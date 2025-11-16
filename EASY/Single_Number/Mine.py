class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        Hashy = {}
        for i, n in enumerate(nums):
            Hashy[n]  = Hashy.get(n,0)+1
        for key, value in Hashy.items():
            if value == 1:
                return key
        # I am using a hash map to store the frequency of each number in the list.
        # I iterate through the list and for each number, I increment its count in the hash map.
        # Then, I iterate through the hash map and return the key (number) whose value
        # is 1, which means it appears only once in the list.
        # The time complexity of this solution is O(n) and the space complexity is O(n).
        