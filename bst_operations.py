
class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None

def insert(root, x):
    if not root:
        return Node(x)
    if x < root.data:
        root.left = insert(root.left, x)
    else:
        root.right = insert(root.right, x)
    return root

def search(root, x):
    if not root or root.data == x:
        return root
    if x < root.data:
        return search(root.left, x)
    return search(root.right, x)

def minimum(root):
    while root.left:
        root = root.left
    return root.data

def maximum(root):
    while root.right:
        root = root.right
    return root.data

root = None
for x in [50, 30, 70, 20, 40, 60, 80]:
    root = insert(root, x)

print("Search 40:", "Found" if search(root, 40) else "Not Found")
print("Minimum:", minimum(root))
print("Maximum:", maximum(root))
