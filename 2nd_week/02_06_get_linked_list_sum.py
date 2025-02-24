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

    # 1. My solution: Use String <-> Int
    def get_whole_int_with_string(self):
        str_number = ""

        current_node = self.head
        while current_node is not None:
            str_number += str(current_node.data)  # int
            current_node = current_node.next

        return int(str_number)

    # 2. Course solution: Arithmetically
    def get_whole_int_with_calculation(self):
        # subsum에 10을 곱해서 옆으로 밀고 다음 숫자를 더함
        sub_sum = 0
        current_node = self.head

        while current_node is not None:
            sub_sum = sub_sum * 10 + current_node.data
            current_node = current_node.next

        return sub_sum

def get_linked_list_sum(linked_list_1, linked_list_2):
    # 각각 온전한 숫자를 만들고 덧셈
    # return linked_list_1.get_whole_int_with_string() + linked_list_2.get_whole_int_with_string()
    return linked_list_1.get_whole_int_with_calculation() + linked_list_2.get_whole_int_with_calculation()


linked_list_1 = LinkedList(6)
linked_list_1.append(7)
linked_list_1.append(8)

linked_list_2 = LinkedList(3)
linked_list_2.append(5)
linked_list_2.append(4)

print(get_linked_list_sum(linked_list_1, linked_list_2))