from typing import Optional

from helper import build_tree


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        # if not root:
        #     return 0
        #
        # def dfs(node, current_sum):
        #     if not node:
        #         return 0
        #
        #     current_sum += node.val
        #     count = 1 if current_sum == targetSum else 0
        #
        #     count += dfs(node.left, current_sum)
        #     count += dfs(node.right, current_sum)
        #
        #     return count
        #
        # return (dfs(root, 0) +
        #         self.pathSum(root.left, targetSum) +
        #         self.pathSum(root.right, targetSum))

        from collections import defaultdict

        prefix_count = defaultdict(int)

        prefix_count[0] = 1

        def dfs(node, curr_sum):
            if not node:
                return 0

            curr_sum += node.val

            needed_sum = curr_sum - targetSum

            count = prefix_count[needed_sum]

            prefix_count[curr_sum] += 1

            count += dfs(node.left, curr_sum)
            count += dfs(node.right, curr_sum)

            # backtrack - remove the current sum before returning to the parent
            prefix_count[curr_sum] -= 1

            return count

        return dfs(root, 0)


sol = Solution()

tree = build_tree([10, 5, -3, 3, 2, None, 11, 3, -2, None, 1])

print(sol.pathSum(tree, targetSum=8))

tree = build_tree([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1])

print(sol.pathSum(tree, targetSum=22))

# Medium
# https://leetcode.com/problems/path-sum-iii/description/
