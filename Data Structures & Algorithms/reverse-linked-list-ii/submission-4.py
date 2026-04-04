# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]):
        if not head:
            return head
        
        prev, cur = None, head
        while cur:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp
        return prev

    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)

        # find head of sublist and prev pointer
        prev = dummy
        for _ in range(left-1):
            prev = prev.next
        sub_head = prev.next
        
        # find tail of sublist and next pointer
        sub_tail = sub_head
        for _ in range(right-left):
            sub_tail = sub_tail.next
        nxt = sub_tail.next

        # detach sublist and reverse it
        prev.next, sub_tail.next = None, None
        new_head = self.reverseList(sub_head)

        # re-attach the reversed list
        prev.next = new_head
        sub_head.next = nxt


        return dummy.next
