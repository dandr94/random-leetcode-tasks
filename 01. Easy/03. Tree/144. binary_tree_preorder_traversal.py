from typing import Optional, List

from helper import build_tree


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def preorder(node):
            if not node:
                return

            res.append(node.val)

            preorder(node.left)

            preorder(node.right)

        preorder(root)

        return res


sol = Solution()

tree = build_tree([1, None, 2, 3])

print(sol.preorderTraversal(tree))

tree = build_tree([1, 2, 3, 4, 5, None, 8, None, None, 6, 7, 9])

print(sol.preorderTraversal(tree))

# Easy
# https://leetcode.com/problems/binary-tree-preorder-traversal/
