#The objective is to insert a node in BST. 
#Note: it does not matter if the tree is balanced or not.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        #when the root node has no child node, it can be understood that the desired location is reached. So a node with the value can be created and returned.
        if not root:
            return TreeNode(val)
        #the variables root.right and root.left is linked to the newly created node as per the condition. As you can see it is done recursively.
        if val > root.val:
            root.right = self.insertIntoBST(root.right, val)
        elif val < root.val:
            root.left = self.insertIntoBST(root.left, val)
        return root
        
