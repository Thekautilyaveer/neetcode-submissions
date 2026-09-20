# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        i, j = head, head

        if head== None:
            return False

        while j.next != None:

            i= i.next
            j = j.next.next
            if j == None:
                return False
            elif i == j:
                return True
        return False

            