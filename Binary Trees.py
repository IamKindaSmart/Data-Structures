class Tree:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def Preorder(root):   #root - left - right
    print(root.data,end="-")
    if root.left != None:
        Preorder(root.left)
    if root.right != None:
        Preorder(root.right)

def Inorder(root):    #left - root - right
    if root.left != None:
        Inorder(root.left)
    print(root.data, end='-')
    if root.right != None:
        Inorder(root.right)

def Postorder(root):   #left - right - root
    if root.left != None:
        Postorder(root.left)
    if root.right != None:
        Postorder(root.right)
    print(root.data, end="-")



#manually creating code
t = Tree("B")
t.right = Tree("D")
t.left = Tree("A")

t.left.left = Tree("E")
t.left.right = Tree("F")


print("This is postorder")
Postorder(t)
print("This is preorder")
Preorder(t)
print("This is inorder")
Inorder(t)
