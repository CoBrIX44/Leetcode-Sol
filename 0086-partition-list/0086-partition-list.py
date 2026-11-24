# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode | None, x: int) -> ListNode | None:
        less_head = ListNode(0)
        greater_head = ListNode(0)
        
        less = less_head
        greater = greater_head
        
        curr = head
        while curr:
            if curr.val < x:
                less.next = curr
                less = less.next
            else:
                greater.next = curr
                greater = greater.next
            curr = curr.next
            
        greater.next = None
        less.next = greater_head.next
        
        return less_head.next