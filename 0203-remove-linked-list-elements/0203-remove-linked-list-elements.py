# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional:
        dummy=ListNode(next=head)
        tail=dummy
        current=head
        while current:
            nxt=current.next
            if current.val==val:
                tail.next=nxt
            else:
                tail=tail.next
            current=current.next
        return dummy.next