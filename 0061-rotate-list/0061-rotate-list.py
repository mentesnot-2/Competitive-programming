# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        val=head
        length=0
        while val:
            val=val.next
            length+=1
        slow=head
        fast=head
        if head is None or head.next is None:
            return head
        k=k%length
        while k>0:
            fast=fast.next
            k-=1
        while fast.next:
            fast=fast.next
            slow=slow.next
        fast.next=head
        head=slow.next
        slow.next=None
        
        return head