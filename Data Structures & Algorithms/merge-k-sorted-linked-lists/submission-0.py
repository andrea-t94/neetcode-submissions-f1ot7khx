# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        ''' use an heap to chose the min val over k list'''
        if len(lists) == 0:
            return None
        dummy = ListNode()
        cur = dummy
        minHeap = []
        cnt = 0
        for lst in lists:
            if lst:
                heapq.heappush(minHeap, (lst.val, cnt, lst))
                cnt += 1 #needed to guarantee that, in case of val tie, we pick one

        while minHeap:
            _, _, node = heapq.heappop(minHeap)
            cur.next = node
            cur = cur.next
            if node.next:
                heapq.heappush(minHeap, (node.next.val, cnt, node.next))
                cnt += 1
        
        return dummy.next
        