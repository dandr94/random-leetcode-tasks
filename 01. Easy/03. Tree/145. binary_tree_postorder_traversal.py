from typing import Optional, List

from helper import build_tree


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def postorder(node):
            if not node:
                return

            postorder(node.left)

            postorder(node.right)

            res.append(node.val)

        postorder(root)

        return res


sol = Solution()

tree = build_tree([1, None, 2, 3])

print(sol.postorderTraversal(tree))

tree = build_tree([1, 2, 3, 4, 5, None, 8, None, None, 6, 7, 9])

print(sol.postorderTraversal(tree))

# Easy
# https://leetcode.com/problems/binary-tree-postorder-traversal/
