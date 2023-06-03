from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        if not head:
            return head

        slow = fast = head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        prev, curr = None, slow.next

        while curr:
            curr.next, prev, curr = prev, curr, curr.next

        slow.next = None

        head1, head2 = head, prev

        while head2:
            head1.next, head1, head2 = head2, head2, head1.next


head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

sol = Solution()
sol.reorderList(head)

node = head
while node:
    print(node.val, end=" -> ")
    node = node.next

# Problem - https://leetcode.com/problems/reorder-list/description/
