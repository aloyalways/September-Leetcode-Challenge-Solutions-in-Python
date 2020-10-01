# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        self.ans=0
        def calculate(bina,node):
            if not node.left and not node.right:
                bina+=str(node.val)
                self.ans+=int(bina,2)
                return
            if node.left:
                calculate(bina+str(node.val),node.left)
            if node.right:
                calculate(bina+str(node.val),node.right)
        calculate("",root)
        return self.ans
