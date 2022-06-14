# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False
        if root.left is None and root.right is None:
            if root.val == targetSum:
                return True
            else:
                return False
        
        def sum_root_to_leaf(root: TreeNode, targetSum, sumToRoot):
            print(root.val, sumToRoot)
            if root.left is None and root.right is None:
                print(sumToRoot + root.val)
                if targetSum == sumToRoot + root.val:
                    return True
            else:
                if root.left is not None:
                    if sum_root_to_leaf(root.left, targetSum, sumToRoot + root.val):
                        return True
                if root.right is not None:
                    if sum_root_to_leaf(root.right, targetSum, sumToRoot + root.val):
                        return True

        
        return sum_root_to_leaf(root, targetSum, 0)
