# Tree Data Structure
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def remove_child(self, child):
        child.parent = None
        self.children.remove(child)

if __name__ == "__main__":
    root = TreeNode(1)
    child1 = TreeNode(2)
    child2 = TreeNode(3)

    root.add_child(child1)
    root.add_child(child2)

    print("Root:", root.data)  # Output: Root: 1
    print("Children of root:", [child.data for child in root.children])  # Output: Children of root: [2, 3]

    root.remove_child(child1)
    print("Children of root after removal:", [child.data for child in root.children])  # Output: Children of root after removal: [3]