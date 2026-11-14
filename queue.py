
queue = []

def enqueue(x):
    queue.append(x)
    print(x, "inserted")

def dequeue():
    if not queue:
        print("Queue is empty")
    else:
        print(queue.pop(0), "removed")

def display():
    print("Queue:", queue)

enqueue(10)
enqueue(20)
enqueue(30)
display()
dequeue()
display()
