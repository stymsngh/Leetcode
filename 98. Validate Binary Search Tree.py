"""
Question: 98. Validate Binary Search Tree
Status: Done
Difficulty: Medium
Author: iamss
Created: 21/08/25
"""

from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        inorder = self.inorder(root)
        for i in range(1, len(inorder)):
            if inorder[i] <= inorder[i - 1]:
                return False
        return True

    def inorder(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        stack, inorder = [], []
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            inorder.append(root.val)
            root = root.right
        return inorder