# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slwptr,fstptr=head,head
        while fstptr and fstptr.next:
            slwptr=slwptr.next
            fstptr=fstptr.next.next
            if slwptr==fstptr:
                return True
        return False
        