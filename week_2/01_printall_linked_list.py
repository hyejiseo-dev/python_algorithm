
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

node = Node(3)
first_node = Node(4)

node.next = first_node # [3] -> [4]
print(node.next.data)

class LinkedList:
    def __init__(self, data): #head node생성
        self.head = Node(data)


    def append(self,data):
        if self.head is None:  #만약 첫 노드 값이 비어있으면 들어온 값을 헤드노드로 바꾸고 중단
            self.head = Node(data)
            return

        #self.head.next = Node(data) #맨앞이 비어있지 않다면 들어온 값에 연결시킴
        cur = self.head  #헤드 노드에서 시작!

        while cur.next is not None:  #맨 끝 노드를 판별! 다음 노드가 None이면 마지막까지 더하기 성공!
            cur = cur.next
            print('cur is', cur.data)
        cur.next = Node(data)

    def print_all(self):
        cur = self.head
        while cur is not None:
            print(cur.data)
            cur = cur.next

    # [3] -> [4] -> [5] -> [6] -> None


linked_list = LinkedList(3)
linked_list.append(4)
linked_list.append(5)
linked_list.print_all()