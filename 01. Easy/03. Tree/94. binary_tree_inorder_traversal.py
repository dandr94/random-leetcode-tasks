from typing import Optional, List

from helper import build_tree


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def inorder(node):
            if not node:
                return

            inorder(node.left)

            res.append(node.val)

            inorder(node.right)

        inorder(root)

        return res


sol = Solution()

root = build_tree([1, None, 2, 3])
print(sol.inorderTraversal(root))

root = build_tree([1, 2, 3, 4, 5, None, 8, None, None, 6, 7, 9])
print(sol.inorderTraversal(root))

# Easy
# https://leetcode.com/problems/binary-tree-inorder-traversal/
