class Dict:
    def __init__(self):
        self.items = [None] * 8

    def put(self,key,value):
        index = hash(key) % len(self.items)
        self.items[index] = value

    def get(self,key):
        index = hash(key) % len(self.items)
        # 같은 값이 나오는 경우? 충돌 발생, 연결리스트로 해결
        return self.items[index]


my_dict = Dict()
my_dict.put("test",3)
print(my_dict.get("test"))