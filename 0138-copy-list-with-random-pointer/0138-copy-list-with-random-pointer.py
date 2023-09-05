"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

    # Step 1: Create copied nodes and insert them after the original nodes
        current = head
        while current:
            copied_node = Node(current.val)
            copied_node.next = current.next
            current.next = copied_node
            current = copied_node.next

        # Step 2: Update random pointers of copied nodes
        current = head
        while current:
            if current.random:
                current.next.random = current.random.next
            current = current.next.next

        # Step 3: Separate the merged list into original and copied lists
        original_head = head
        copied_head = head.next
        copied_current = copied_head

        while copied_current.next:
            original_head.next = copied_current.next
            original_head = original_head.next
            copied_current.next = original_head.next
            copied_current = copied_current.next

        original_head.next = None  # Set the last node of the copied list to None

        return copied_head

