from uuid import getnode


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self, value):
        self.head = Node(value)

    def append(self, value):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(value)

    def print_all(self):
        cur = self.head
        print("<all nodes>")
        while cur is not None:
            print(cur.data)
            cur = cur.next

    def get_node(self, index):
        cur = self.head
        for _ in range(0, index):
            cur = cur.next
        # print("index", index, ":", cur.data)
        return cur

    def add_node(self, index, value):
        new_node = Node(value)

        if index == 0:
            new_node.next = self.head
            self.head = new_node
            return

        # index != 0
        previous_node = self.get_node(index-1) # 삽입 직전 노드로 감

        # 변경
        new_node.next = previous_node.next
        previous_node.next = new_node

        return

linked_list = LinkedList(5)
linked_list.append(12)
linked_list.append(17)
linked_list.print_all()

linked_list.add_node(3, 7)
linked_list.print_all()
