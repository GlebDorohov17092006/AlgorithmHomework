# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        start = ListNode()
        iter_lists, buffer = start, None

        if head is None:
            return head

        while not(head.next is None):
            if (buffer is None):
                if head.val==head.next.val:
                    buffer = head.val
                else:
                    iter_lists.next = head
                    iter_lists = iter_lists.next
                head = head.next
            else:
                if buffer!=head.next.val:
                    buffer = None
                head = head.next

        if buffer is None:
            iter_lists.next = head
            iter_lists = iter_lists.next
        else:
            if buffer==head.val:
                iter_lists.next = head.next
        return start.next