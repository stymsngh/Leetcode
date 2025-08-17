"""
Question: 23. Merge k Sorted Lists
Status: Done
Difficulty: Hard
Author: iamss
Created: 17/08/25
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

import heapq
from typing import Optional, List


class Pair:
    def __init__(self, list_val, ll):
        self.list_val = list_val
        self.ll = ll

    def __lt__(self, other):
        return self.list_val < other.list_val


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []

        # Add all list first elements with the list to the heap
        for ll in lists:
            if ll:
                heapq.heappush(heap, Pair(ll.val, ll))

        # Construct the heap
        merged_ll = ListNode(-1)
        temp = merged_ll

        while len(heap) > 0:
            pair = heapq.heappop(heap)
            l_val, ll = pair.list_val, pair.ll

            temp.next = ListNode(l_val)
            temp = temp.next

            # Add next element of this list back to heap
            if ll.next:
                heapq.heappush(heap, Pair(ll.next.val, ll.next))

        return merged_ll.next
