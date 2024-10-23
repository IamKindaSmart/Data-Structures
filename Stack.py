class stack:
    def __init__(self,n):
        self.stack=[]
        self.n=n
    #Method
    def push(self,item): #add item to the stack
        if len(self.stack) < self.n:
            self.stack.append(item)

        else:
            print("Stack Overflow")

    #Pop
    def pop(self): #remove item from the stack
        if len(self.stack) <= 0:
            print("Stack Underflow")

        else:
            self.stack.pop(-1) # Delete the last item

    def top(self): #tells the top item from the stack
        if len(self.stack) == 0:
            print("Stack Underflow")

        else:
            return self.stack[-1] #Returns the last value from the stack
    
    #custom methods
    def display(self):
        print(self.stack)
    
    def size(self):
        print(len(self.stack))

#example
st = stack(4)
st.push(3)
st.push(8)
st.push(1)
st.push(0)
st.push(7)
st.display()
st.pop()
st.display()
print(st.top())
st.size()