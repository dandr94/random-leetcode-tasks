from typing import Optional

from helper import build_tree


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def is_mirror(left_subtree, right_subtree):
            if not left_subtree and not right_subtree:
                return True

            if not left_subtree or not right_subtree:
                return False

            val_equal = left_subtree.val == right_subtree.val
            outer_equal = is_mirror(left_subtree.left, right_subtree.right)
            inner_equal = is_mirror(left_subtree.right, right_subtree.left)

            return val_equal and outer_equal and inner_equal

        return is_mirror(root.left, root.right)


sol = Solution()

tree = build_tree([1, 2, 2, 3, 4, 4, 3])
print(sol.isSymmetric(tree))

tree = build_tree([1, 2, 2, None, 3, None, 3])
print(sol.isSymmetric(tree))

# Easy
# https://leetcode.com/problems/symmetric-tree/
