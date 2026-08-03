# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root) :
        right = []
        if root is None:
            return right
        queue = deque([root])

        while queue:
            length = len(queue)

            for i in range(length):
                node = queue.popleft()

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

                if  i == length -1 :
                    right.append(node.val)


        
        return right