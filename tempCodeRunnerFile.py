if not root.left or not root.right:
                return left+right+1
            return min(left,right)+1