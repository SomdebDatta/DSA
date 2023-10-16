# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        carry, add = 0, 0
        ans_list = list()
        while l1 and l2:
            add = l1.val + l2.val + carry
            carry = (l1.val + l2.val + carry) // 10
            if carry:
                add -= 10
            l1 = l1.next
            l2 = l2.next
            ans_list.append(add)

        if l1 is None and l2 is not None:
            while l2:
                add = l2.val + carry
                carry = (l2.val + carry) // 10
                if carry:
                    add -= 10
                ans_list.append(add)
                l2 = l2.next
        elif l2 is None and l1 is not None:
            while l1:
                add = l1.val + carry
                carry = (l1.val + carry) // 10
                if carry:
                    add -= 10
                ans_list.append(add)
                l1 = l1.next
        if carry:
            ans_list.append(carry)
        print(ans_list)

        ans_ll = ListNode(ans_list[0])
        ans_ll_head = ans_ll

        for i in range(1, len(ans_list)):
            ans_ll.next = ListNode(ans_list[i])
            ans_ll = ans_ll.next
        return ans_ll_head
