# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        depths = []
        
        def find_leaf(root, depth):
            if root.left is None and root.right is None:
                depths.append(depth)
                return
            else:
                depth += 1
                if root.left:
                    find_leaf(root.left, depth)
                if root.right:
                    find_leaf(root.right, depth)
        find_leaf(root, 1)
        return min(depths)
