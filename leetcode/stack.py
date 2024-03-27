from collections import deque

stack = deque()

stack.append("a")
stack.append("b")
stack.append("c")

print(f"Initial stack - f{stack}")
print(stack.pop())
print(f"Stack now - f{stack}")
