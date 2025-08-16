"""
Question: Container With Most Water
Status: Done
Difficulty: Medium
Author: iamss
Created: 16/08/25
"""
from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_water_area = 0
        left, right = 0, len(height)-1

        while left <= right:
            max_water_area = max(max_water_area, min(height[left], height[right])*(right - left))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_water_area
