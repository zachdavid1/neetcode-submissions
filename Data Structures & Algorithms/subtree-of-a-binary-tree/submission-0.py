# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        queue = deque([root])
        while queue:
            curr = queue.popleft()
            if curr:
                queue.append(curr.left)
                queue.append(curr.right)
                if curr.val == subRoot.val:
                    if self.same_tree(curr, subRoot):
                        return True
        return False


    def same_tree(self, root1, root2):
        if not root1 and not root2:
            return True
        if not root1 or not root2:
            return False
        if root1.val != root2.val:
            return False
        
        l = self.same_tree(root1.left, root2.left)
        r = self.same_tree(root1.right, root2.right)

        return l and r