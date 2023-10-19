from typing import Optional


# Definition for a Node.
class Node:
    def __init__(self, x: int, next: "Node" = None, random: "Node" = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: "Optional[Node]") -> "Optional[Node]":
        old_to_new = dict()
        start = head
        start_ans = ans = Node(0)
        while start:
            old_to_new[start] = Node(start.val)
            start = start.next

        start = head
        while start:
            ans.next = old_to_new.get(start)
            ans.next.random = old_to_new.get(start.random)
            ans = ans.next
            start = start.next
        return start_ans.next

    def copyRandomList2(self, head: "Optional[Node]") -> "Optional[Node]":
        head_copy = head

        while head_copy:
            temp = Node(head_copy.val)
            temp.next = head_copy.next
            head_copy.next = temp
            head_copy = head_copy.next

        head_copy = head
        while head_copy:
            if head_copy.random:
                head_copy.next.random = head_copy.random.next
                head_copy = head_copy.next.next

        head_copy = head
        ans = head_copy.next
        while head_copy:
            temp = head_copy.next
            head_copy.next = head_copy.next.next
            head_copy = temp

        return ans
