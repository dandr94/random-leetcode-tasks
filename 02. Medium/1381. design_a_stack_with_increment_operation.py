class CustomStack:
    def __init__(self, maxSize: int):
        self.max_size = maxSize
        self.stack = []

    def push(self, x: int) -> None:
        if not self.is_full:
            self.stack.append(x)

    def pop(self) -> int:
        if not self.is_empty:
            return self.stack.pop()

        return -1

    def increment(self, k: int, val: int) -> None:
        for i in range(min(k, len(self.stack))):
            self.stack[i] += val

    @property
    def is_full(self):
        return len(self.stack) == self.max_size

    @property
    def is_empty(self):
        return len(self.stack) == 0


stk = CustomStack(3)
stk.push(1)
stk.push(2)
print(stk.pop())
stk.push(2)
stk.push(3)
stk.push(4)
stk.increment(5, 100)
print(stk.stack)
stk.increment(2, 100)
print(stk.stack)
print(stk.pop())
print(stk.pop())
print(stk.pop())
print(stk.pop())

# Problem - https://leetcode.com/problems/design-a-stack-with-increment-operation/description/
