class MinStack(object):

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.stack.append(val)
        val = min(val, self.min_stack[-1] if self.min_stack else val)
        self.min_stack.append(val)

    def pop(self):
        """
        :rtype: None
        """
        self.stack.pop()
        self.min_stack.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.min_stack[-1]

mStack = MinStack()
print(mStack.push(2))
print(mStack.push(0))
print(mStack.push(3))
print(mStack.push(0))
print(mStack.getMin())
print(mStack.pop())
print(mStack.getMin())
print(mStack.pop())
print(mStack.getMin())
print(mStack.pop())
print(mStack.getMin())
