# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        if not root: return 0
        #returns the height of the proble,
        def dfs(curr):
            if not curr: 
                return 0
        left = dfs(curr.left)
        right = dfs(curr.right)
        self.res = max(self.res, left+righr)
    
        return 1 + max(left, right)
        