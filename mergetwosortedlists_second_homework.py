from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]: 
        start = ListNode()
        iter_lists = start
        while list1 and list2:
            if list1.val < list2.val:
                iter_lists.next = list1
                list1 = list1.next
            else:
                iter_lists.next = list2
                list2 = list2.next
            iter_lists = iter_lists.next
        while list1:
            iter_lists.next = list1
            list1 = list1.next
            iter_lists = iter_lists.next
        while list2:
            iter_lists.next = list2
            list2 = list2.next
            iter_lists = iter_lists.next
        return start.next
        