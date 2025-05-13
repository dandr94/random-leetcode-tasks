from typing import Optional

from helper import build_tree


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def get_leaves(node):
            if not node:
                return []

            if not node.left and not node.right:
                return [node.val]

            return get_leaves(node.left) + get_leaves(node.right)

        return get_leaves(root1) == get_leaves(root2)


sol = Solution()

tree_1 = build_tree([3, 5, 1, 6, 2, 9, 8, None, None, 7, 4])

tree_2 = build_tree([3, 5, 1, 6, 7, 4, 2, None, None, None, None, None, None, 9, 8])

print(sol.leafSimilar(tree_1, tree_2))

tree_1 = build_tree([1, 2, 3])

tree_2 = build_tree([1, 3, 2])

print(sol.leafSimilar(tree_1, tree_2))

# Easy
# https://leetcode.com/problems/leaf-similar-trees/
