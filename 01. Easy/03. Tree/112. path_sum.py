from typing import Optional

from helper import build_tree


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # def dfs(node, remaining_sum):
        #     if not node:
        #         return False
        #
        #     if not node.left and not node.right:
        #         return remaining_sum == node.val
        #
        #     left = dfs(node.left, remaining_sum - node.val)
        #     right = dfs(node.right, remaining_sum - node.val)
        #
        #     return left or right
        #
        # return dfs(root, targetSum)

        if not root:
            return False

        if not root.left and not root.right:
            return targetSum == root.val

        return self.hasPathSum(root.left, targetSum - root.val) or self.hasPathSum(root.right, targetSum - root.val)


sol = Solution()

tree = build_tree([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1])

print(sol.hasPathSum(tree, targetSum=22))

tree = build_tree([1, 2, 3])

print(sol.hasPathSum(tree, targetSum=5))

tree = build_tree([])

print(sol.hasPathSum(tree, targetSum=0))

# Easy
# https://leetcode.com/problems/path-sum/description/
