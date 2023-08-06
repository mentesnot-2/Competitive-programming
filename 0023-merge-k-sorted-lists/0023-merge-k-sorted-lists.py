import heapq

class ListNodeWrapper:
    def __init__(self, node):
        self.node = node

    def __lt__(self, other):
        return self.node.val < other.node.val

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def mergeKList(arr, K):
            queue = []
            for i in range(K):
                if arr[i] != None:
                    heapq.heappush(queue, ListNodeWrapper(arr[i]))
            dummy = ListNode(0)
            last = dummy
            while queue:
                wrapper = heapq.heappop(queue)
                curr = wrapper.node
                last.next = curr
                last = last.next
                if curr.next != None:
                    heapq.heappush(queue, ListNodeWrapper(curr.next))
            return dummy.next
        return mergeKList(lists, len(lists))
