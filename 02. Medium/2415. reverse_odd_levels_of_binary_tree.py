from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        def dfs(node_1: TreeNode, node_2: TreeNode, curr_level: int) -> None:
            if not node_1 or not node_2:
                return

            if curr_level % 2 != 0:
                node_1.val, node_2.val = node_2.val, node_1.val

            dfs(node_1.left, node_2.right, curr_level + 1)
            dfs(node_1.right, node_2.left, curr_level + 1)

        dfs(root.left, root.right, 1)

        return root

# Problem - https://leetcode.com/problems/reverse-odd-levels-of-binary-tree/
