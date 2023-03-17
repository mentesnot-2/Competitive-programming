# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode()
        tail=dummy
        val=[]
        curr=head
        while curr:
            val.append(curr.val)
            curr=curr.next
        val=sorted(val)
        for i in val:
            tail.next=ListNode(i)
            tail=tail.next
        # print(dummy)
        head=dummy.next
        dummy.next=None
        return head
        
            
        