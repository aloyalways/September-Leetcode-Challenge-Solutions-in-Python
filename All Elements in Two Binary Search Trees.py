# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        root1_node=[]
        root2_node=[]
        def allnode1(node):
            if node is None:
                return
            root1_node.append(node.val)
            allnode1(node.left)
            allnode1(node.right)
        def allnode2(node):
            if node is None:
                return
            root2_node.append(node.val)
            allnode2(node.left)
            allnode2(node.right)
        allnode1(root1)
        allnode2(root2)
        return sorted(root1_node+root2_node)
