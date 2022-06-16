# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        tr = []
        def traverse(root):
            if root is not None:
                if root.left:
                    traverse(root.left)
                tr.append(root.val)
                if root.right:
                    traverse(root.right)
        traverse(root)
        return tr
    
