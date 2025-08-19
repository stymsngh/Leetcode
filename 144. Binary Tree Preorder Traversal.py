"""
Question: 144. Binary Tree Preorder Traversal
Status: Done
Difficulty: Easy
Author: iamss
Created: 19/08/25
"""
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Preorder -> Root Left Right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        preorder, stack = [], []
        if not root:
            return preorder

        stack.append(root)
        while stack:
            root = stack.pop()
            preorder.append(root.val)

            if root.right:
                stack.append(root.right)
            if root.left:
                stack.append(root.left)

        return preorder
