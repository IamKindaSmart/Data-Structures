class QueueUsingStacks:
    def __init__(self):
        self.input_stack = []  # Stack for adding stuff
        self.output_stack = []  # Stack for removing stuff

    def is_empty(self):
        return not self.input_stack and not self.output_stack

    def enqueue(self, item):
        self.input_stack.append(item)
        print(f"{item} added to the queue")

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty. Can't remove anything.")
            return None
        if not self.output_stack:
            while self.input_stack:
                self.output_stack.append(self.input_stack.pop())
        item = self.output_stack.pop()
        print(f"{item} removed from the queue")
        return item

    def front(self):
        if self.is_empty():
            print("Queue is empty. No front item.")
            return None
        if not self.output_stack:
            while self.input_stack:
                self.output_stack.append(self.input_stack.pop())
        return self.output_stack[-1]

    def rear(self):
        if self.is_empty():
            print("Queue is empty. No rear item.")
            return None
        if self.input_stack:
            return self.input_stack[-1]
        return self.output_stack[0]

    def display(self):
        if self.is_empty():
            print("Queue is empty.")
        else:
            print("Queue:", self.output_stack[::-1] + self.input_stack)


# Example usage
q = QueueUsingStacks()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.display()  # Queue: [10, 20, 30]
q.dequeue()  # 10 removed from the queue
q.display()  # Queue: [20, 30]
print("Front:", q.front())  # Front: 20
print("Rear:", q.rear())    # Rear: 30
