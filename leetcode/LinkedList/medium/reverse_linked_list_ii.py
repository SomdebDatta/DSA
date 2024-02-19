from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(
        self, head: Optional[ListNode], left: int, right: int
    ) -> Optional[ListNode]:
        og_head = head
        if right == left:
            return og_head
        index = 1
        while index != left - 1 and left != 1:
            head = head.next
            index += 1
        start = head
        prev = start.next
        curr = prev.next
        head = head.next
        while index != right - 1:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
            index += 1
            # print(prev.val, curr.val, temp.val, index)
        head.next = curr
        start.next = prev
        return og_head
