# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        index_list = list()
        # curr=head
        while head is not None:
            index_list.append(head)
            if head.next in index_list:
                return True
            head = head.next
        return False
