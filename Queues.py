class Queue:
    def __init__(self):
        self.queue=[]

    def enqueue(self,item):
        self.queue.append(item)
        print("Item Added")
    
    def is_empty(self):
        return len(self.queue)==0
    
    def dequeue(self):
        if self.is_empty():
            print("Queue is empty")
        item = self.queue.pop(0)
        print("f{item} deleted")
        return item
    
    def front(self):
        if self.is_empty():
            print("Queue is empty")
        return self.queue[0]
    
    def rear(self):
        if self.is_empty():
            print("Queue is empty")
        return self.queue[-1] #-Ve index number starts with -1
    
    def display(self):
        if self.is_empty():
            print("Queue is empty")
        else:
            print(self.queue)

q = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(40)
q.enqueue(50)
q.enqueue(60)
q.enqueue(70)

q.dequeue()
q.display()

print(f"Front item is {q.front()}")
print(f"Rear item is {q.rear()}")