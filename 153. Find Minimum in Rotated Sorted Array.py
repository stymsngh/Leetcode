"""
Question: 153. Find Minimum in Rotated Sorted Array
Status: Done
Difficulty: Medium
Author: iamss
Created: 19/08/25
"""

from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        low, high = 0, len(nums)-1
        mini = float('inf')
        while low <= high:
            mid = low + (high-low)//2
            mini = min(nums[mid], mini)

            # Check for sorted side
            if nums[low] <= nums[mid]:
                mini = min(mini, nums[low])
                low = mid+1
            else:
                mini = min(mini, nums[mid])
                high = mid-1
        return mini
