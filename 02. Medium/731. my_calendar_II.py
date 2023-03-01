class Node:
    def __init__(self, low: int, high: int):
        self.start = low
        self.end = high
        self.overlap = 1
        self.left = None
        self.right = None


class MyCalendarTwo:

    def __init__(self):
        self.tree = Node(-1, -1)

    def book(self, start: int, end: int) -> bool:
        if self.scan(self.tree, start, end - 1) and self.insert(self.tree, start, end - 1):
            return True

        return False

    def insert(self, tree: Node, start: int, end: int) -> Node:
        if start > end:
            return tree

        if tree is None:
            return Node(start, end)

        if end < tree.start:
            tree.left = self.insert(tree.left, start, end)

        elif tree.end < start:
            tree.right = self.insert(tree.right, start, end)

        else:
            tree.left = self.insert(tree.left, min(tree.start, start), max(tree.start, start) - 1)
            tree.right = self.insert(tree.right, min(tree.end, end) + 1, max(tree.end, end))
            tree.overlap += 1
            tree.start = max(tree.start, start)
            tree.end = min(tree.end, end)
        return tree

    def scan(self, tree: Node, start: int, end: int) -> bool | Node:
        if tree is None or start > end:
            return True
        if end < tree.start:
            return self.scan(tree.left, start, end)
        if tree.end < start:
            return self.scan(tree.right, start, end)

        if tree.overlap == 2:
            return False

        return self.scan(tree.left, min(tree.start, start), max(tree.start, start) - 1) \
            and self.scan(tree.right,
                          min(tree.end,
                              end) + 1,
                          max(tree.end,
                              end))


myCalendarTwo = MyCalendarTwo()
print(myCalendarTwo.book(10, 20))
print(myCalendarTwo.book(50, 60))
print(myCalendarTwo.book(10, 40))
print(myCalendarTwo.book(5, 15))
print(myCalendarTwo.book(5, 10))
print(myCalendarTwo.book(25, 55))

# Problem - https://leetcode.com/problems/my-calendar-ii/description/
