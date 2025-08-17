"""
Question: 55. Jump Game
Status: Done
Difficulty: Medium
Author: iamss
Created: 17/08/25
"""

from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        target_idx = len(nums) - 1
        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >= target_idx:
                target_idx = i

        return target_idx == 0