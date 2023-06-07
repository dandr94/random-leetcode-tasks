# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        if not head:
            return 0

        num = ''

        while head:
            num += str(head.val)
            head = head.next

        return int(num, 2)


head = ListNode(1)
head.next = ListNode(0)
head.next.next = ListNode(1)

sol = Solution()
print(sol.getDecimalValue(head))

# Problem - https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/description/
