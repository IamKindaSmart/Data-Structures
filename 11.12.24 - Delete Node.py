class Tree:
    def __init__(self,key):
        self.val=key
        self.left=None
        self.right=None

def insert(root, key):
    #if the tree is empty - this node becomes root node, return
    if root is None:
        return Tree(key)
    
    if key < root.val:
        root.left = insert(root.left,key)
    else:
       root.right = insert(root.right,key)

    return root

def delete(root,key):
    #base case: If root is None:
    if root is None:
        return root
    
    #otherwise go down the tree and find the node
    if key < root.val:
        delete(root.left,key)
    
    elif key>root.val:
        delete(root.right,key)

    else:
        #case 1: when the node is a leaf node
        if root.left is None and root.right is None:
            return None
        
        #case 2: when the node has 1 child node
        if root.left is None:
            return root.right
        
        elif root.right is None:
            return root.left
        
        #case 3: when the node has 2 children node
        #(Get the inorder successor (smallest node in the right subtree))
        temp = findInordersuccessor(root.right)

        #replace root value
        root.val = temp.val

        #Delete the inorder successor
        root.right = delete(root.right,temp.val)

    return root

def findInordersuccessor(node):
    current = node
    while current.left is not None:
        current = current.left

    return current

#inorder traversal = left, root, right (sorted)
def inorder(root):
    if root:
        inorder(root.left)
        print(root.val,end='-')
        inorder(root.right)

#example
root = None
root = insert(root, 50)
root = insert(root, 30)
root = insert(root, 26)
root = insert(root, 21)
root = insert(root, 38)
root = insert(root, 20)

print("Inorder traversal before deleting")
inorder(root)

#delete 70
root = delete(root,30)
print("\n Inorder traversal after deleting 30")

inorder(root)