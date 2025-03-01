class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# push(1): [1]
# push(2): [2] -> [1]
# -> 매번 Head 변경..(?)

class Stack:

    def __init__(self):
        self.head = None

    def push(self, value):
        if self.head is None:
            self.head = Node(value)
        else:
            current_head = self.head
            self.head = Node(value)
            self.head.next = current_head
        print("after push, head: ", self.head.data)
        return

    # pop 기능 구현
    def pop(self):
        if self.is_empty():
            print("stack is empty")
            return
        # remove head and switch
        current_head = self.head
        self.head = self.head.next
        return current_head.data

    def peek(self):
        if self.is_empty():
            print("stack is empty")
            return
        return self.head.data

    # isEmpty 기능 구현
    def is_empty(self):
        return self.head is None


stack = Stack()
stack.push(1)
# stack.push(2)
print(stack.peek()) # 2
print(stack.pop()) # 2
stack.is_empty() # false
stack.pop() # 1
