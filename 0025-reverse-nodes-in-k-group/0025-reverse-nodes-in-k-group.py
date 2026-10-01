class Solution:
    def reverseKGroup(self, head: ListNode | None, k: int) -> ListNode | None:
        
        node = head
        count = 0
        while node and count < k:
            node = node.next
            count += 1
        
        if count < k:
            return head  
        
        prev = None
        curr = head
        for _ in range(k):
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        head.next = self.reverseKGroup(curr, k)
        
        return prev