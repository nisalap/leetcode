# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        n = 0
        sum = 0
        while True:
            sum += int(l1.val) * 10 ** n
            if l1.next is None:
                break
            l1 = l1.next
            n += 1
        n = 0
        while True:
            sum += int(l2.val) * 10 ** n
            if l2.next is None:
                break
            l2 = l2.next
            n += 1
            
        def prep_list(val, node):
            if val < 10:
                node.val = val
                node.next = None
                return
            else:
                node.val = val % 10
                node.next = ListNode()
                return prep_list(val // 10, node.next)
        
        node = ListNode()
        prep_list(sum, node)
        return node
