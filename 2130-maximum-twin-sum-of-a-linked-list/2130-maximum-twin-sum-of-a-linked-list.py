# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        val=[]
        curr=head
        targ=head
        while curr:
            val.append(curr.val)
            curr=curr.next
        val=val[::-1]
        total=0
        i=0
        while targ:
            total=max(total,val[i]+targ.val)
            targ=targ.next
            i+=1
        return total

        