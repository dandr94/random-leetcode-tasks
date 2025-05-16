from typing import Optional

from helper import build_tree, tree_to_list


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)

        if root.val > val:
            root.left = self.insertIntoBST(root.left, val)
        else:
            root.right = self.insertIntoBST(root.right, val)

        return root


sol = Solution()

tree = build_tree([4, 2, 7, 1, 3])

print(tree_to_list(sol.insertIntoBST(tree, val=5)))

tree = build_tree([40, 20, 60, 10, 30, 50, 70])

print(tree_to_list(sol.insertIntoBST(tree, val=25)))

tree = build_tree([4, 2, 7, 1, 3, None, None, None, None, None, None])

print(tree_to_list(sol.insertIntoBST(tree, val=5)))

# Medium
# https://leetcode.com/problems/insert-into-a-binary-search-tree/description/
