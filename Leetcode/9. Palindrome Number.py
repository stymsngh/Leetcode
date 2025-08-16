"""
Question: 9. Palindrome Number
Status: Done
Difficulty: Medium
Author: iamss
Created: 16/08/25
"""

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x > 9 and x%10 == 0):
            return False

        revNum = 0
        while x > revNum:
            revNum = revNum * 10 + x % 10
            x //= 10

        return x == revNum or x == revNum//10