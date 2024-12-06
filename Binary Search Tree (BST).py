class Tree:
    def __init__(self,key):
        self.left=None
        self.right=None
        self.val=key

def insert(root, key): #key is the new value that we want to insert
    #empty tree causes the first node to become the root
    if root is None:
        return Tree(key)
    
    #otherwise recur down the tree
    if key < root.val: #if new value <  root
        root.left = insert(root.left, key)
    
    else:
        root.right= insert(root.right, key)

    #return the root
    return root

def search(root,key):
    if root is None or root.val == key:
        return root
    if key < root.val:
        return search(root.left,key)
    else:
        return search(root.right,key)

def Inorder(root):
    if root:   #left - root - right
        Inorder(root.left)
        print(root.val, end='-')
        Inorder(root.right)


t= None
t= insert(t,6)
t= insert(t,3)
t= insert(t,8)
t= insert(t,0)
t= insert(t,1)

Inorder(t)

found_node = search(t,0)
if found_node:
    print("\n Element found")
else:
    print("\n Not found")
