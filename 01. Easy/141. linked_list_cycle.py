from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False

        one_stepper = two_stepper = head

        while two_stepper and two_stepper.next:
            one_stepper = one_stepper.next
            two_stepper = two_stepper.next.next

            if one_stepper == two_stepper:
                return True

        return False

# Problem - https://leetcode.com/problems/linked-list-cycle/
