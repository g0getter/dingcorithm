class MaxHeap:
    def __init__(self):
        self.items = [None]

    # 1. 맨 끝에 추가
    # 2. 부모와 비교
    # 3. 대소관계 틀리면 교체
    # 4. 더 이상 변경하지 않을 때(부모가 자식보다 클 때)까지 2-3 반복
    # array로 이진 트리 구현: 0번째는 비우기
    def insert(self, value):
        self.items.append(value)

        index = len(self.items)-1
        while index//2 >= 1 and self.items[index//2] < self.items[index]: # 부모가 작으면 (단, 0번째까지 가지 않도록 >=1)
            self.items[index//2], self.items[index] = self.items[index], self.items[index//2] # 교체
            # 다음 것 비교
            index = index // 2

        return

max_heap = MaxHeap()
max_heap.insert(3)
max_heap.insert(4)
max_heap.insert(2)
max_heap.insert(9)
print(max_heap.items)  # [None, 9, 4, 2, 3] 가 출력되어야 합니다!