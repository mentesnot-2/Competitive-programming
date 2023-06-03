# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode(next=head)
        tail=dummy
        current=head
        stack=[]
        while current:
            if stack:
                while stack and stack[-1]<current.val:
                    top=stack.pop()
                stack.append(current.val)
            elif stack==[]:
                stack.append(current.val)
            current=current.next
       
        
        for i in stack:
            tail.next=ListNode(i)
            tail=tail.next
        return dummy.next
        