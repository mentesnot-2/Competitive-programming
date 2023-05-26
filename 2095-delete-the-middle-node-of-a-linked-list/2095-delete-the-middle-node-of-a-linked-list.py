# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        lenlist=0
        current=start=node=head
        while current:
            lenlist+=1
            current=current.next
        middle=lenlist//2
        if middle<1:
            return None
        else:
            counter=0
            while start:
                if counter==middle:
                    previous.next=node.next
                    node.next=None
                    break
                previous=node
                node=node.next
                counter+=1
        return head
        