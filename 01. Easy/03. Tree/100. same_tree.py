from typing import Optional

from helper import build_tree


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True

        if not p or not q:
            return False

        val_equal = p.val == q.val
        left_equal = self.isSameTree(p.left, q.left)
        right_equal = self.isSameTree(p.right, q.right)

        return val_equal and left_equal and right_equal


sol = Solution()

tree_p = build_tree([1, 2, 3])
tree_q = build_tree([1, 2, 3])
print(sol.isSameTree(tree_p, tree_q))

tree_p = build_tree([1, 2])
tree_q = build_tree([1, None, 2])
print(sol.isSameTree(tree_p, tree_q))

tree_p = build_tree([1, 2, 1])
tree_q = build_tree([1, 1, 2])
print(sol.isSameTree(tree_p, tree_q))

# Easy
# https://leetcode.com/problems/same-tree/
