#Maxheap
#2018015027 김한탁
#Maxheap 삭제 연

class MaxHeap:
    def __init__(self):
        self.heap = []
        self.heap.append(0)

    def size(self):
        return len(self.heap) - 1

    def isEmpty(self):
        return self.size() == 0

    def parent(self, i):
        return self.heap[i // 2]

    def left(self, i):
        return self.heap[i * 2]

    def right(self, i):
        return self.heap[i * 2 + 1]

    def display(self, msg = 'Max Heap : '):
        print(msg, self.heap[1:])

    def insert(self, n):
        self.heap.append(n)
        i = self.size()
        while i != 1 and n > self.parent(i):
            self.heap[i] = self.parent(i)
            i = i // 2
        self.heap[i] = n

    def delete(self):
        parent = 1
        child = 2
        if not self.isEmpty():
            hroot = self.heap[1]
            last = self.heap[self.size()]
            while child <= self.size():
                if child < self.size() and self.left(parent) < self.right(parent):
                    child += 1
                if last >= self.heap[child]:
                    break
                self.heap[parent] = self.heap[child]
                parent = child
                child *= 2

            self.heap[parent] = last
            self.heap.pop(-1)
            return hroot
        
heap=MaxHeap()
data=[2,5,4,8,9,3,7,3]
print("[삽입 연산] : " + str(data))
for elem in data:
    heap.insert(elem)
heap.display('[삽입 후]: ')
heap.delete()
heap.display('[삭제 후]: ')
heap.delete()
heap.display('[삭제 후]: ')
