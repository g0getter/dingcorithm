# 같은 index가 나왔을 때 충돌 해결 방법
class LinkedTuple:
    def __init__(self):
        self.items = []

    def add(self, key, value):
        self.items.append((key, value)) ####

    def get(self, key):
        for k, v in self.items:
            if k == key:
                return v

class Dict:
    def __init__(self):
        # self.items = [None] * 8
        self.items = [LinkedTuple()] * 8

    def put(self, key, value):
        index = hash(key) % len(self.items)
        self.items[index].add(key, value)

    def get(self, key):
        return self.items[hash(key) % len(self.items)].get(key)


my_dict = Dict()
my_dict.put("test", 3)
print(my_dict.get("test"))  # 3이 반환되어야 합니다!
