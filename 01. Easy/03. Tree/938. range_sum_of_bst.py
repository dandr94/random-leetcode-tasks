from typing import Optional

from helper import build_tree


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        # res = []
        #
        # def dfs(node):
        #     if not node:
        #         return 0
        #
        #     if low <= node.val <= high:
        #         res.append(node.val)
        #
        #     dfs(node.left)
        #
        #     dfs(node.right)
        #
        # dfs(root)
        #
        # return sum(res)

        res = [0]

        def dfs(node):
            if not node:
                return

            if low <= node.val <= high:
                res[0] += node.val

            # In a Binary Search Tree, for any given node:
            # All values in the left subtree are less than the node's value.
            # All values in the right subtree are greater than the node's value.
            if node.val > low:
                dfs(node.left)
            if node.val < high:
                dfs(node.right)

        dfs(root)

        return res[0]


sol = Solution()

tree = build_tree([10, 5, 15, 3, 7, None, 18])

print(sol.rangeSumBST(tree, low=7, high=15))

tree = build_tree([10, 5, 15, 3, 7, 13, 18, 1, None, 6])

print(sol.rangeSumBST(tree, low=6, high=10))

# Easy
# https://leetcode.com/problems/range-sum-of-bst/
