#Algorithm Implementations in Python
#Algorithms are step-by-step procedures or formulas for solving problems.
#1. Sorting Algorithms
# Sorting algorithms are used to arrange elements in a specific order (ascending or descending).    
#1. Bubble Sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
# Example usage:
arr = [64, 34, 25, 12, 22, 11, 90]
sorted_arr = bubble_sort(arr)
print(sorted_arr)

#2. Searching Algorithms
# Searching algorithms are used to find specific elements in a collection of data.
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

# Example usage:
arr = [64, 34, 25, 12, 22, 11, 90]
target = 22
index = linear_search(arr, target)
print(index)  # Output: 4

#3. Graph Algorithms
# Graph algorithms are used to solve problems related to graphs, such as finding the shortest path or detecting cycles.
#3.1 Dijkstra's Algorithm   
# Dijkstra's algorithm is used to find the shortest path from a source node to all other nodes in a weighted graph.
import heapq

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    pq = [(0, start)]
    
    while pq:
        current_distance, current_node = heapq.heappop(pq)
        
        if current_distance > distances[current_node]:
            continue
            
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
    
    return distances
# Example usage:
graph = {   
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}
distances = dijkstra(graph, 'A')
print(distances)

#3.2 Depth-First Search (DFS)
# Depth-First Search is an algorithm for traversing or searching tree or graph data structures. 
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)
    return visited
# Example usage:
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}
visited = dfs(graph, 'A')
print(visited)

#3.3 Breadth-First Search (BFS)
# Breadth-First Search is an algorithm for traversing or searching tree or graph data structures. It explores all the neighbor nodes at the present depth prior to moving on to the nodes at the next depth level.
from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)

    while queue:
        current = queue.popleft()
        for neighbor in graph[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return visited

# Example usage:
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}
visited = bfs(graph, 'A')
print(visited)  


#4. Conclusion
# In this module, we have implemented some common algorithms in Python, including sorting algorithms, searching algorithms, and graph algorithms. These algorithms are fundamental to computer science and are widely used in various applications. 

