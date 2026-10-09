# Custom Data Structures in Python
# This file contains implementations of custom data structures that can be used in Python programs. 
# 1. Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
# Example usage:
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)

# 2. Stack
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
        else:
            raise IndexError("pop from empty stack")
    
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("peek from empty stack")
    
    def size(self):
        return len(self.items)

# 3. Queue
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
        else:
            raise IndexError("dequeue from empty queue")
    
    def size(self):
        return len(self.items)
    
# 4. Binary Tree
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
# 5. Graph
class Graph:
    def __init__(self):
        self.adjacency_list = {}
    
    def add_vertex(self, vertex):
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = []
    
    def add_edge(self, vertex1, vertex2):
        if vertex1 in self.adjacency_list and vertex2 in self.adjacency_list:
            self.adjacency_list[vertex1].append(vertex2)
            self.adjacency_list[vertex2].append(vertex1)  # For undirected graph

# Example usage:
# Creating a graph  
graph = Graph()
graph.add_vertex("A")
graph.add_vertex("B")
graph.add_edge("A", "B")
