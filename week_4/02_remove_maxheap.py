class MaxHeap:
    def __init__(self):
        self.items = [None]

    def insert(self, value):
        self.items.append(value)
        cur_index = len(self.items) - 1

        while cur_index > 1:  # cur_index 가 1이 되면 정상을 찍은거라 다른 것과 비교 안하셔도 됩니다!
            parent_index = cur_index // 2
            if self.items[parent_index] < self.items[cur_index]:
                self.items[parent_index], self.items[cur_index] = self.items[cur_index], self.items[parent_index]
                cur_index = parent_index
            else:
                break


    def delete(self):
        # 구현해보세요!
        self.items[1] , self.items[-1] = self.items[-1] , self.items[1]
        prev_max = self.items.pop() #맨 끝 원소 반환
        # 여기부터 힙의 규칙을 지키기 위한 코드
        cur_index = 1

        while cur_index <= len(self.items)-1:
            left_child_index = cur_index * 2  #왼쪽 자식
            right_child_index = cur_index * 2 + 1 #오른쪽 자식
            max_index = cur_index

            #왼쪽 자식이 있고, 왼쪽 자식이 부모노드 보다 더 클 경우
            if left_child_index <= len(self.items)-1 and self.items[left_child_index] > self.items[cur_index]:
                max_index = left_child_index

            # 오른쪽 자식이 있고, 오른쪽 자식이 부모노드 보다 더 클 경우
            if right_child_index <= len(self.items)-1 and self.items[right_child_index] > self.items[cur_index]:
                max_index = right_child_index

            if max_index == cur_index:  # 지금 제일 큰 수가 있고, 교체가 불필요하면
                break

            #왼쪽과 오른쪽을 비교해서 더 큰 수랑 바꿔준다!
            self.items[cur_index], self.items[max_index] = self.items[max_index], self.items[cur_index]


        return prev_max


max_heap = MaxHeap()
max_heap.insert(8)
max_heap.insert(6)
max_heap.insert(7)
max_heap.insert(2)
max_heap.insert(5)
max_heap.insert(4)
print(max_heap.items)  # [None, 8, 6, 7, 2, 5, 4]
print(max_heap.delete())  # 8 을 반환해야 합니다!
print(max_heap.items)  # [None, 7, 6, 4, 2, 5]