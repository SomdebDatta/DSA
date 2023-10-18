from typing import Optional


# Definition for a Node.
class Node:
    def __init__(self, x: int, next: "Node" = None, random: "Node" = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: "Optional[Node]") -> "Optional[Node]":
        if not head:
            return head

        pos_list = list()

        ans_ll = Node(0)
        ans_ll_head = ans_ll
        og_head = head
        while head:
            ans_ll.next = Node(head.val)
            pos_list.append(head)
            head = head.next
            ans_ll = ans_ll.next
        ans_ll_head = ans_ll_head.next
        print(len(pos_list))
        head_copy = ans_ll_head
        for i in range(len(pos_list)):
            ans_ll_head.random = pos_list[i].random.val
            ans_ll_head = ans_ll_head.next
        return head_copy
