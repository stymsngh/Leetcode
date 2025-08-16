"""
Question: Two Sum.py
Status: Done
Difficulty: Easy
Author: iamss
Created: 16/08/25
"""
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # BRUTE FORCE
        # ans = []
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             ans.append(i)
        #             ans.append(j)
        # return ans

        # OPTIMISED
        value_mapper = {}
        for idx, val in enumerate(nums):
            to_find = target - val
            if to_find in value_mapper:
                return [idx, value_mapper[to_find]]
            value_mapper[val] = idx
        return []
