#Bianary Tree
'''
1.Hirarchical Data structure
2.Topmost element is know as the root of tree
3.every node can have at most 2 children in binary tree
4.can't access elements randomly using index
5.common traversal methods:
    a.preorder(root)  -- print-left-right
    b.postorder(Root) -- left-right-print
    c.inorder(root)   -- left-print-right

'''

#Binary Tree implementation
#just remember word Root where it belongs
'''
        1  
    2       3
4 

Inorder ===  left root right   4,2,1,3 
preorder === root left right   1,2,4,3
postorder == left right root   4,2,3,1

'''

#code examples for inorder preorder postorder
'''
class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def preorder(root):
    if root:
        print(root.data, end =" ")
        preorder(root.left)
        preorder(root.right)

def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end =" ")
        inorder(root.right)

def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.data,end =" ")

#create a binary tree

root = Node(1)
root.left =Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print("Preorder traversal:")
preorder(root)

print("\nInorder traversal:")
inorder(root)

print("\nPostorder traversal:")
postorder(root)

'''    

#Advantages

'''
1.Can represent data with some relatioship
2.Insertion and search are much more efficient

'''

#Disadvantages
'''
1.Sorting is difficult
2.Not much flexible
'''

































