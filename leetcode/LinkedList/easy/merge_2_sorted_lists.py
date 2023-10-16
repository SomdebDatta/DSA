# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        merged_ll = ListNode()
        merged_ll_head = merged_ll
        while list1 or list2:
            if list1 is None:
                merged_ll.next = list2
                list2 = list2.next

            elif list2 is None:
                merged_ll.next = list1
                list1 = list1.next
            elif list1.val < list2.val:
                merged_ll.next = list1
                list1 = list1.next
            else:
                merged_ll.next = list2
                list2 = list2.next
            merged_ll = merged_ll.next
        return merged_ll_head.next
