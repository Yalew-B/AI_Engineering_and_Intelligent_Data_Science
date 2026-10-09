# Linked List Data Structure
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def append(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete(self, data):
        if self.is_empty():
            return

        if self.head.data == data:
            self.head = self.head.next
            return

        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next
            
    def search(self, data):
        current = self.head
        while current:
            if current.data == data:
                return True
            current = current.next
        return False
    
if __name__ == "__main__":
    linked_list = LinkedList()
    linked_list.append(1)
    linked_list.append(2)
    linked_list.append(3)
    linked_list.prepend(0)

    print("Linked List after appending and prepending:")
    current = linked_list.head
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("None")

    linked_list.delete(2)
    print("Linked List after deleting 2:")
    current = linked_list.head
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("None")

    print("Searching for 3 in the Linked List:", linked_list.search(3))
    print("Searching for 4 in the Linked List:", linked_list.search(4))
        