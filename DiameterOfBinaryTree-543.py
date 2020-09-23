# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def height(self,root,hei):
        if root == None:
            return 0
        if root in hei:
            return hei[root]
        hei[root] = 1+max(self.height(root.right,hei),self.height(root.left,hei))
        return hei[root]
    
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        hei = {}
        if root == None:
            return 0
        lh = self.height(root.left,hei)
        rh = self.height(root.right,hei)
        return max(lh+rh,self.diameterOfBinaryTree(root.left),self.diameterOfBinaryTree(root.right))
        
