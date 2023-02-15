# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode()
        tail=dummy
        current1=list1
        current2=list2
        while current1 and current2:
            if current1.val<current2.val:
                tail.next=current1
                
                tail=current1
                current1=current1.next
            elif current1.val>current2.val:
                tail.next=current2
                tail=current2
                current2=current2.next
            else:
                tail.next=current1
                tail=current1
                current1=current1.next
        while current1:
            tail.next=current1
            tail=current1
            current1=current1.next
        while current2:
            tail.next=current2
            tail=current2
            current2=current2.next
        return dummy.next
    