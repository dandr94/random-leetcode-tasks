from typing import Optional

from helper import build_tree, tree_to_list


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return None

        if root.val == val:
            return root

        if root.val > val:
            return self.searchBST(root.left, val)
        else:
            return self.searchBST(root.right, val)


sol = Solution()

tree = build_tree([4, 2, 7, 1, 3])

print(tree_to_list(sol.searchBST(tree, val=2)))

tree = build_tree([4, 2, 7, 1, 3])

print(tree_to_list(sol.searchBST(tree, val=5)))

# Easy
# https://leetcode.com/problems/search-in-a-binary-search-tree/description/
