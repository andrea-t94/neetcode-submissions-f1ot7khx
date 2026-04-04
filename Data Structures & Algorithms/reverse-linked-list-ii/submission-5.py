# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        ''' one pass '''
        dummy = ListNode(0, head)

        # identify head of sublist and its pointer
        # will be later attached to the new head
        leftPrev, cur = dummy, head
        for _ in range(left-1):
            leftPrev, cur = leftPrev.next, cur.next
        
        # now reverse it
        prev = None
        for _ in range(right-left+1):
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp
        
        # now prev points to the new head that needs to be attached to leftPrev
        # but leftPrev points to the old head (now tail) 
        # that needs to be attached to next node, which cur points to
        leftPrev.next.next = cur
        leftPrev.next = prev


        return dummy.next
