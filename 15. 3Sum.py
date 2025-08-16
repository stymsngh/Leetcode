"""
Question: 15. 3Sum
Status: Done
Difficulty: Medium
Author: iamss
Created: 16/08/25
"""

from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []

        ans = set()
        nums.sort()
        for i in range(len(nums)-2):
            left, right = i+1, len(nums)-1
            while left < right:
                summ = nums[i] + nums[left] + nums[right]
                if summ == 0:
                    ans.add((nums[i], nums[left], nums[right]))
                    left+=1
                    right-=1
                    while left < right and nums[left] == nums[left-1]:
                        left += 1
                    while right > left and nums[left] == nums[right+1]:
                        right -= 1
                elif summ < 0:
                    left+=1
                else:
                    right-=1
        return list(ans)