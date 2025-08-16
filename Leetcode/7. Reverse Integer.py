"""
Question: Reverse Integer
Status: Done
Difficulty: Easy
Author: iamss
Created: 16/08/25
"""

class Solution:
    def reverse(self, x: int) -> int:
        mini, maxi = -2 ** 31, 2 ** 31 - 1
        sign = False
        if x < 0:
            sign = True
            x = abs(x)
        revNum = 0
        while x:
            revNum = revNum * 10 + x % 10
            if revNum < mini or revNum > maxi:
                return 0
            x //= 10
        return -revNum if sign else revNum
