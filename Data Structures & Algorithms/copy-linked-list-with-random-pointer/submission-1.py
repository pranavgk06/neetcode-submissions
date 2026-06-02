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
        
        oldtocopy = {None : None}
        curr = head

        # pass 1 writing every node value into hashmap
        while curr:
            copy = Node(curr.val)
            oldtocopy[curr] = copy
            curr = curr.next
        
        # reset curr and start at og list and take next and random pointers
        curr = head
        while curr:
            copy = oldtocopy[curr]
            copy.next = oldtocopy[curr.next]
            copy.random = oldtocopy[curr.random]
            curr = curr.next
        return oldtocopy[head]

        