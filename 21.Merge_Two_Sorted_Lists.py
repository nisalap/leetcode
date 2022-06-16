# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        sorted_data = []
        if l1 == None:
            if l2 == None:
                return l1
            else:
                return l2
        else:
            if l2 == None:
                return l1
            else:
                node = l1
                while node.next != None:
                    sorted_data.append(node.val)
                    node = node.next
                sorted_data.append(node.val)
                node = l2
                while node.next != None:
                    sorted_data.append(node.val)
                    node = node.next
                sorted_data.append(node.val)
                sorted_data.sort(reverse=True)
                next = None
                for each in sorted_data:
                    a = ListNode(each, next)
                    next = a
                return a
