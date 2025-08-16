"""
Question: 128. Longest Consecutive Sequence
Status: Done
Difficulty: Medium
Author: iamss
Created: 16/08/25
"""

from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nset = set(nums)
        longest = 0
        for num in nset:
            if num-1 not in nset:
                count = 0
                current = num
                while current in nset:
                    count += 1
                    current += 1
                longest = max(longest, count)
        return longest