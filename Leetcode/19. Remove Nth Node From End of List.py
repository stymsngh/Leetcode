"""
Question: 19. Remove Nth Node From End of List
Status: Done
Difficulty: Medium
Author: iamss
Created: 16/08/25
"""

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = self.length(head)
        node_idx_to_del = length - n
        prev = None
        k = 0
        temp = head
        while k < node_idx_to_del:
            prev = temp
            temp = temp.next
            k += 1

        if temp and prev:
            prev.next = temp.next
            return head
        elif not prev:
            return head.next
        else:
            return None

    def length(self, head: Optional[ListNode]) -> int:
        if not head:
            return 0
        return 1 + self.length(head.next)
