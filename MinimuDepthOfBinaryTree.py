class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class solution:
    def minDepth(self, root):
            
            if not root:
                return 0
            left=self.minDepth(root.left)
            right=self.minDepth(root.right)
            if not root.left or not root.right:
                return left+right+1
            return min(left,right)+1
root=TreeNode(3)
root.left=TreeNode(9)
root.right=TreeNode(20)
root.right.left=TreeNode(15)
root.right.right=TreeNode(7)
solutions=solution()
z=solutions.minDepth(root)
print(z)