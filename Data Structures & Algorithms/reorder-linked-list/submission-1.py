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
        
        second_list = slow.next
        slow.next = None

        while second_list:
            temp = second_list.next
            second_list.next = prev
            prev = second_list
            second_list = temp
        
        while prev:
            temp_curr = curr.next
            temp_prev = prev.next

            curr.next = prev
            prev.next = temp_curr

            curr = temp_curr
            prev = temp_prev
        

        