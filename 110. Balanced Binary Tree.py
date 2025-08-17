"""
Question: 110. Balanced Binary Tree
Status: Done
Difficulty: Easy
Author: iamss
Created: 17/08/25
"""
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        lheight = self.height(root.left)
        rheight = self.height(root.right)

        if abs(lheight - rheight) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right):
            return True

        return False

    def height(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        return 1 + max(self.height(root.left), self.height(root.right))