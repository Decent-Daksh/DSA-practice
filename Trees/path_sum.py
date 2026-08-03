# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root , targetSum):
        if root is None:
            return False
        
        if (root.left is None and root.right is None):
            return targetSum - root.val == 0
       
        L = self.hasPathSum(root.left ,targetSum - root.val) 
        R = self.hasPathSum(root.right , targetSum - root.val )

        return L or R