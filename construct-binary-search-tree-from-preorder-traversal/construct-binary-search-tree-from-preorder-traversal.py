# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        def traverse(node, value):
            if value < node.val:
                if node.left:
                    traverse(node.left, value)
                else:
                    node.left = TreeNode(value)
            else:
                if node.right:
                    traverse(node.right, value)
                else:
                    node.right = TreeNode(value)
                    
        root = TreeNode(preorder.pop(0))
        for value in preorder:
            traverse(root, value)
        return root
        
        