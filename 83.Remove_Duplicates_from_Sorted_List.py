# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        first = True
        head1 = None
        while True:
            if first: 
                head1 = head
                first = False
            if head is None:
                return head1
            if head.val is None:
                return head1
            if head.next is None:
                return head1
            if head.val == head.next.val:
                while  head.next is not None and (head.val == head.next.val):
                    head.next = head.next.next
                head = head.next
            else:
                head = head.next
