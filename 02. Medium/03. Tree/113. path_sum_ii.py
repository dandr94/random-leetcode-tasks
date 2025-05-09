from typing import Optional, List

from helper import build_tree


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        # Copying
        # res = []
        #
        # def dfs(node, path, current_sum):
        #     if not node:
        #         return
        #
        #     path = path + [node.val]
        #
        #     current_sum += node.val
        #
        #     if not node.left and not node.right and current_sum == targetSum:
        #         res.append(path)
        #     else:
        #         dfs(node.left, path, current_sum)
        #         dfs(node.right, path, current_sum)
        #
        # dfs(root, [], 0)
        #
        # return res

        # Backtrack
        res = []

        def dfs(node, path, current_sum):
            if not node:
                return

            path.append(node.val)

            current_sum += node.val

            if not node.left and not node.right and current_sum == targetSum:
                res.append(list(path))
            else:
                dfs(node.left, path, current_sum)
                dfs(node.right, path, current_sum)

            path.pop()  # Backtrack to previous state

        dfs(root, [], 0)

        return res


sol = Solution()

tree = build_tree([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1])

print(sol.pathSum(tree, targetSum=22))

tree = build_tree([1, 2, 3])

print(sol.pathSum(tree, targetSum=5))

tree = build_tree([1, 2])

print(sol.pathSum(tree, targetSum=0))

# Medium
# https://leetcode.com/problems/path-sum-ii/
