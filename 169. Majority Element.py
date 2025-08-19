"""
Question: 169. Majority Element
Status: Done
Difficulty: Easy
Author: iamss
Created: 19/08/25
"""
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        votes, majority_candidate = 0, 0
        for i in range(len(nums)):
            if votes == 0:
                majority_candidate = nums[i]
                votes = 1
            else:
                if nums[i] == majority_candidate:
                    votes += 1
                else:
                    votes -= 1

        # Check if majority_candidate is the actual winner
        count = 0
        for i in range(len(nums)):
            if nums[i] == majority_candidate:
                count += 1

        return majority_candidate if count >= len(nums) // 2 else -1
