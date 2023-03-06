# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        res=""
        current=head
        total=0
        while current:
            res+=str(current.val)
            current=current.next
        for i in range(len(res)):
            if res[i]=="1":
                total=total + 1 * 2**(len(res)-1-i)
            else:
                total=total + 0 * 2**(len(res)-1-i)
        return total
        