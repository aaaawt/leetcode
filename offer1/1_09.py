class CQueue:

    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def appendTail(self, value: int) -> None:
        self.in_stack.append(value)

    def deleteHead(self) -> int:
        if not self.out_stack:
            if not self.in_stack:
                return -1
            else:
                while self.in_stack:
                    self.out_stack.append(self.in_stack.pop())
        return self.out_stack.pop()


obj = CQueue()
print(obj.deleteHead())
obj.appendTail(5)
obj.appendTail(2)
print(obj.deleteHead())
print(obj.deleteHead())
