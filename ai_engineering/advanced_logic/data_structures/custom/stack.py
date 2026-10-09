# Stack Data Structure
class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None

if __name__ == "__main__":
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)

    print("Top item:", stack.peek())  # Output: Top item: 3
    print("Pop:", stack.pop())        # Output: Pop: 3
    print("Top item after pop:", stack.peek())  # Output: Top item after pop: 2