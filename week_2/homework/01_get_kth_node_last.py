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
        # 구현해보세요!
        node = self.head
        cnt = 1
        while node.next is not None: #한칸씩 이동하며 증가
            node = node.next
            cnt += 1
        end = cnt - k #전체 - k번째
        node = self.head
        for i in range(end):
            node = node.next
        return node


linked_list = LinkedList(6)
linked_list.append(7)
linked_list.append(8)

print(linked_list.get_kth_node_from_last(2).data)  # 7이 나와야 합니다!