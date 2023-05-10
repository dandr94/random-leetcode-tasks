from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        cur, prev = head, None

        while cur:
            cur.next, prev, cur = prev, cur, cur.next

        return prev

# Problem - https://leetcode.com/problems/reverse-linked-list/
