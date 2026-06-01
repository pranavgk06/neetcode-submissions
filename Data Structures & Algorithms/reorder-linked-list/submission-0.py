# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fast = head
        slow = head
        curr = head
        prev = None

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        new_temp = slow.next
        slow.next = None

        while new_temp:
            temp = new_temp.next
            new_temp.next = prev
            prev = new_temp
            new_temp = temp

        while prev:
            temp_curr = curr.next
            temp_prev = prev.next

            curr.next = prev
            prev.next = temp_curr

            curr = temp_curr
            prev = temp_prev
        

        