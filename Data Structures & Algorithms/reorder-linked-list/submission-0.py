# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #finding mid point
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        #2nd list
        second = slow.next
        slow.next = None
        first = head

        #reversing 2nd
        prev, curr = None, second
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp

        #prev is head of 2nd

        while prev:
            tmp1 = head.next
            tmp2 = prev.next
            head.next = prev
            prev.next = tmp1
            head, prev = tmp1, tmp2
        


        


        