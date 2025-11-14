#Binary Search Tree
'''
1.Binart tree with the additional restriction
2.Restriction:
   a.left child must always be less than root node
   b.Right child must always be greater than root node
3.Insertion,Deletion,Search is much more efficient than a binary tree

'''

#Binary search tree implementation
'''
1. Insert element into binary search tree
2. Search element into binary search tree
3. Delete element from binary search tree
'''

#code for Binary search tree -insertion code -- inorder
'''
class Node:
    
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right =None

def insert(root,key):
    if root is None:
        return Node(key)
    
    if key < root.data:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)

    return root

def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end = " ")
        inorder(root.right)

root = None

values = [50,30,20,40,70,60,80]

for v in values:
    root = insert(root, v)

print("Inorder traversal of BST")
inorder(root)

'''

#FULL BST CODE (Insert + Search + Traversals)

'''
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# INSERT into BST
def insert(root, key):
    if root is None:
        return Node(key)

    if key < root.data:
        root.left = insert(root.left, key)
    elif key > root.data:
        root.right = insert(root.right, key)

    return root


# SEARCH in BST
def search(root, key):
    if root is None or root.data == key:
        return root

    if key < root.data:
        return search(root.left, key)

    return search(root.right, key)


# TRAVERSALS
def preorder(root):
    if root:
        print(root.data, end=" ")
        preorder(root.left)
        preorder(root.right)

def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)

def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.data, end=" ")


# ------------------------------------------------------------
# CREATE BST and TEST
# ------------------------------------------------------------

# Create the BST
root = None
values = [50, 30, 20, 40, 70, 60, 80]

for val in values:
    root = insert(root, val)


print("Inorder Traversal (Sorted):")
inorder(root)

print("\nPreorder Traversal:")
preorder(root)

print("\nPostorder Traversal:")
postorder(root)

# SEARCH
key = 60
result = search(root, key)
print("\n\nSearching for:", key)

if result:
    print("Key found:", result.data)
else:
    print("Key not found")

'''

#advanages
'''
1.Can represent data with some relationship
2.Insertion and search are much more efficient
'''

# dis-advantages
'''
1.Sorting is difficult
2.Not much flexible

'''































