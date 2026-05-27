# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        fast = head
        slow = head
        prev = None
        curr = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        while slow:
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp
        
        while prev:
            if (curr.val != prev.val):
                return False
            curr = curr.next
            prev = prev.next
        return True
        

        