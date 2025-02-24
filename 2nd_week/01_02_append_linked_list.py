# LinkedList, Node 구현하기

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value: int):
        self.head = Node(value)

    def append(self, value: int):
        current_node = self.head
        while current_node.next is not None:
            current_node = current_node.next

        # last node(tail)
        current_node.next = Node(value)

    # prints all nodes in `self`
    def print_all(self):
        current_node = self.head
        while current_node is not None:
            print("value:", current_node.value, ", next:", "Null" if current_node.next is None else current_node.next.value)
            current_node = current_node.next

linked_list = LinkedList(3)
linked_list.append(4)
linked_list.append(10)
# print(node.value)
linked_list.print_all()
