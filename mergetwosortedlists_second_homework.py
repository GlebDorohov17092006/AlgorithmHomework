from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1==None:
            return list2
        elif list2==None:
            return list1
        else:
            buffer = []
            while not(list1 is None) and not(list2 is None):
                if list1.val < list2.val:
                    if len(buffer) > 0: 
                        buffer[-1].next = list1
                    buffer.append(list1)
                    list1 = list1.next
                    
                else:
                    if len(buffer) > 0:
                        buffer[-1].next = list2
                    buffer.append(list2)
                    list2 = list2.next
            while not(list1 is None):
                if len(buffer) > 0: 
                    buffer[-1].next = list1
                buffer.append(list1)
                list1 = list1.next
            while not(list2 is None):
                if len(buffer) > 0: 
                    buffer[-1].next = list2
                buffer.append(list2)
                list2 = list2.next
            
            return buffer[0]
        