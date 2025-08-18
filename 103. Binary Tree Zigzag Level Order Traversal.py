"""
Question: 103. Binary Tree Zigzag Level Order Traversal
Status: Done
Difficulty: Medium
Author: iamss
Created: 18/08/25
"""
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        level_ord = []
        if not root:
            return []

        direction = False

        q = deque([root])
        while q:
            level = []
            for i in range(len(q)):
                node = q.popleft()

                if not direction: # Left -> Right
                    level.append(node.val)
                else: # Right -> Left
                    level.insert(0, node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            direction = not direction
            level_ord.append(level)
        return level_ord

