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

    def get_kth_node_from_last(self, k):
        # stack에 하나씩 넣고 k-1번째 pop한 결과값 or array의 k-1번째에 접근
        # 어쨌든 끝까지 가야함. O(N)은 필수적.
        array = [] # or stack
        cur = self.head

        while cur is not None:
            array.append(cur)
            cur = cur.next

        return array[k-1]


linked_list = LinkedList(6)
linked_list.append(7)
linked_list.append(8)

print(linked_list.get_kth_node_from_last(3).data)  # 7이 나와야 합니다!

# 다른 방법(수업의 답안 중 하나): 길이를 몰라도 가능 (그러나 어쨌든 끝까지 가야하므로 O(N)임)
# head에서 시작하는 `slow`와 그로부터 k만큼 떨어진 `fast`를 정의하고 같이 이동 - fast가 끝에 갈 때까지.
# 그때 slow를 반환.