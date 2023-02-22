class myStack:

    def __init__(self):
        self.stack = []

    # Creating a new stack
    def create_stack(self):
        self.stack = []

    # Checking if stack is empty
    def is_empty(self):
        return len(self.stack) == 0

    # Adding an item to the stack
    def push(self, item):
        self.stack.append(item)
        print("Pushed item: " + str(item))

    # Removing an item from the stack
    def pop(self):
        if self.is_empty():
            return "Stack is empty"
        else:
            return self.stack.pop()

    # Displaying the stack elements
    def show(self):
        print("The stack elements are:")
        for item in self.stack:
            print(item)


myStack1 = myStack()
# stack_var = myStack1.create_stack()
myStack1.push(str(10))
myStack1.push( str(20))
myStack1.push( str(30))
myStack1.push( str(40))

print("popped item: " + myStack1.pop())
myStack1.show()
