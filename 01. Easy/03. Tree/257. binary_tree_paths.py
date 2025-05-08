from typing import Optional, List

from helper import build_tree


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res = []

        def dfs(node, path):
            if not node:
                return

            path_value = path + str(node.val)

            if not node.left and not node.right:
                res.append(path_value)
            else:
                dfs(node.left, path_value + '->')
                dfs(node.right, path_value + '->')

        dfs(root, '')

        return res


sol = Solution()

tree = build_tree([1, 2, 3, None, 5])

print(sol.binaryTreePaths(tree))

tree = build_tree([1])

print(sol.binaryTreePaths(tree))

# Easy
# https://leetcode.com/problems/binary-tree-paths/description/
