
stack = []

def push(x):
    stack.append(x)
    print(x, "pushed")

def pop():
    if not stack:
        print("Stack is empty")
    else:
        print(stack.pop(), "popped")

def display():
    print("Stack:", stack)

push(10)
push(20)
push(30)
display()
pop()
display()
