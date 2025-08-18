"""
Question: 101. Symmetric Tree
Status: Done
Difficulty: Easy
Author: iamss
Created: 18/08/25
"""

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        def checkSym(left: Optional[TreeNode], right: Optional[TreeNode]):
            if not left and not right:
                return True
            if not left or not right:
                return False
            if left.val == right.val and checkSym(left.left, right.right) and checkSym(left.right, right.left):
                return True
            else:
                return False

        if root.left and root.right:
            return checkSym(root.left, root.right)
        elif not root.left and not root.right:
            return True

        return False