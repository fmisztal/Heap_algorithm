import heapq
class MaxHeap:
    def __init__(self, num_of_children):
        self.heap = []
        self.size = 0
        self.num_of_children = num_of_children

    def insert(self, value):
        self.heap.append(value)
        self.size += 1
        if self.size > 0:
            self.heapify_up(int(self.size-1))

    def heapify_up(self, index):
        parent = int((index-1) / self.num_of_children)
        if self.heap[parent] < self.heap[index]:
            self.heap[parent], self.heap[index] = self.heap[index], self.heap[parent]
            self.heapify_up(parent)

    def heapify_down(self, index):
        largest_index = index

        for i in range(self.num_of_children):
            child_index = self.num_of_children * index + 1 + i

            if child_index < self.size and self.heap[child_index] > self.heap[largest_index]:
                largest_index = child_index

        if largest_index != index:
            swap = self.heap[index]
            self.heap[index] = self.heap[largest_index]
            self.heap[largest_index] = swap

            self.heapify_down(largest_index)

    def heap_extract_max(self):
        if self.size < 1:
            print("Heap empty")
            return
        max = self.heap[0]
        self.heap[0] = self.heap[self.size-1]
        self.size -= 1
        self.heapify_down(0)
        return max

    def display(self):
        print(self.heap)
        self._display(0, 0, 0)

    def _display(self, index, pref, level):
        if index < self.size:
            print((" " * 5) * level + str(pref+1) + ": " + str(self.heap[index]))
            for i in range(self.num_of_children):
                self._display(self.num_of_children * index + 1 + i, i, level+1)


if __name__ == '__main__':
    h = MaxHeap(2)

    import random
    random.seed(45)

    values = [random.randint(1, 100) for _ in range(20)]
    for v in values:
        h.insert(v)

    h.display()

    # print(h.heap_extract_max())
    #
    # h.display()
    #
    # print("\n---------")
    #
    # h2 = MaxHeap(5)
    # for v in values:
    #     h2.insert(v)
    # h2.display()
    #
    # print("\n---------")

    # max_heap = [-x for x in values]
    # heapq.heapify(max_heap)
    # sorted_arr = [-x for x in max_heap]
    # print(sorted_arr)