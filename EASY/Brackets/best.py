class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        rulesMap = {")":"(","]":"[", "}":'{'}
        for n in s:
            if n in rulesMap:
                if stack and stack[-1]== rulesMap[n]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(n)
        return True if not stack else False        
        
        # I am usinog stack data structure to solve this problem.
        # I have created a map to store the closing and opening brackets.
        # I am iterating through the string and checking if the character is in the map.
        # If it is in the map, I check if the stack is not empty and the top of the stack is equal to the corresponding opening bracket.
        # If it is, I pop the top of the stack.
        # If it is not, I return False.
        # If the character is not in the map, I push it onto the stack.
        # Finally, I check if the stack is empty. If it is, I return True, otherwise I return False.