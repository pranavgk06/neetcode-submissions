# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        curr = head
        prev = dummy

        for _ in range(left-1):
            curr = curr.next
            prev = prev.next
        
        temp_prev = prev
        temp_curr = curr

        for _ in range(right-left+1):
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        temp_prev.next = prev
        temp_curr.next = curr

        return dummy.next

        