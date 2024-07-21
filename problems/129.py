"""
Sum Root to Leaf Numbers

You are given the root of a binary tree containing digits from 0 to 9 only.
Each root-to-leaf path in the tree represents a number.
For example, the root-to-leaf path 1 -> 2 -> 3 represents the number 123.

Return the total sum of all root-to-leaf numbers.
Test cases are generated so that the answer will fit in a 32-bit integer.

A leaf node is a node with no children.
"""

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # Time: O(n) Space: O(h)
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfs(root, num):
            if not root: return 0

            num = num * 10 + root.val
            if root.left is None and root.right is None:
                return num

            return dfs(root.left, num) + dfs(root.right, num)

        return dfs(root, 0)
