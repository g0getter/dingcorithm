class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, value):
        # head와 tail이 비어 있으면 value로 설정
        # 아니면 tail의 next가 가리키고 tail이 value가 되게 설정
        new_node = Node(value)
        if self.head and self.tail:
            self.tail.next = new_node
            self.tail = new_node
        else:
            self.head = self.tail = new_node
        return

    def dequeue(self):
        if self.is_empty():
            print("queue is empty")
            return

        node_to_delete = self.head
        self.head = self.head.next

        return node_to_delete.data

    def peek(self):
        if self.is_empty():
            print("queue is empty")
            return

        return self.head.data

    def is_empty(self):
        return self.head is None # 어차피 head를 가장 먼저 반환하므로 tail까지는 안 봐도 될 것

queue = Queue()
print(queue.is_empty())
queue.enqueue(1)
queue.enqueue(2)
print(queue.peek())
print(queue.dequeue())
print("dequeue:",queue.dequeue())
print("peek:",queue.peek())