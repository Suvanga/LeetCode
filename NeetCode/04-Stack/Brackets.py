class Solution:
    def isValid(self, s: str) -> bool:
        stacky = [] 
        hashy = {")":"(", 
                    "]":"[]",
                    "}":"{}"}
        for c in s:
            if c in hashy:
                if stacky and stacky[-1] == hashy[c]:
                    stacky.pop()
                else: 
                    return False
            else:
                stacky.append(c)

        return True if not stacky else False
    
