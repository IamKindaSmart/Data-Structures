class Tree:
    def __init__(self,key):
        self.left=None
        self.Right=None
        self.data=key

def insert(root, key): #key is the new value that we want to insert
    #empty tree causes the first node to become the root
    if root is None:
        return Tree(root)
    
    #otherwise recur down the tree
    if key < root.data: #if new value <  root
        root.left = insert(root.left, key)
    
    else:
        root.right= insert(root.right, key)

    #return the root
    return root

def Inorder(root):    #left - root - right
    Inorder(root.left)
    print(root.data, end='-')
    Inorder(root.right)


t = Tree(8)
insert(t,6)
insert(t,3)
insert(t,8)
insert(t,0)
insert(t,1)

Inorder(t)