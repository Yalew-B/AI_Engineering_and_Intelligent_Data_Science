# Queue Data Structure
class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        return None

    def front(self):
        if not self.is_empty():
            return self.items[0]
        return None

    def rear(self):
        if not self.is_empty():
            return self.items[-1]
        return None

if __name__ == "__main__":
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)

    print("Front item:", queue.front())  # Output: Front item: 1
    print("Rear item:", queue.rear())    # Output: Rear item: 3

    print("Dequeue:", queue.dequeue())    # Output: Dequeue: 1
    print("Front item after dequeue:", queue.front())  # Output: Front item after dequeue: 2
    