class Tree:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

#manually creating code
t = Tree("B")
t.right = Tree("D")
t.left = Tree("A")

t.left.left = Tree("E")
t.left.right = Tree("F")