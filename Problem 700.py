# the objective of this problem is to return the subtree of the target value(including that node) if it exists in a BST.
#approach is done recursively to reach the time-complexity O(log n). can also be done recusively but you will need to maintain a stack for that.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        #return if the root node has no branches.
        if not root:
            return None


        if val > root.val:
            return self.searchBST(root.right, val)
        elif val < root.val:
            return self.searchBST(root.left, val)
        else:
            return root
        
