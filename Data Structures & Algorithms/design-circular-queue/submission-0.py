class Node:
    def __init__(self, val: int):
        self.val = val
        self.next = None

class MyCircularQueue:

    def __init__(self, k: int):
        self.front = self.rear = None
        self.size = 0
        self.capacity = k

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False

        node = Node(value)
        if self.isEmpty():
            self.rear = self.front = node
            self.rear.next = self.front
        else:
            self.rear.next = node
            self.rear = node
            self.rear.next = self.front
        self.size += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        if self.front == self.rear:
            self.front = self.rear = None
        else:
            self.front = self.front.next
            self.rear.next = self.front
        self.size -= 1
        return True

    def Front(self) -> int:
        if self.front:
            return self.front.val
        else:
            return -1

    def Rear(self) -> int:
        if self.rear:
            return self.rear.val
        else:
            return -1

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.capacity


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()