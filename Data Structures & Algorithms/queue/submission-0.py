class Node:
    def __init__(self, val: int):
        self.val = val
        self.next = None
        self.prev = None

class Deque:
    
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def isEmpty(self) -> bool:
        return (self.size == 0)

    def append(self, value: int) -> None:
        node = Node(value)
        if self.isEmpty():
            self.head = self.tail = node
        else:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node
        self.size += 1


    def appendleft(self, value: int) -> None:
        node = Node(value)
        if self.isEmpty():
            self.head = self.tail = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node
        self.size += 1

    def pop(self) -> int:
        if self.isEmpty():
            return -1
        value = self.tail.val
        self.tail = self.tail.prev
        self.size -= 1
        if self.size > 0:
            self.tail.next = None
        return value

    def popleft(self) -> int:
        if self.isEmpty():
            return -1
        value = self.head.val
        self.head = self.head.next
        self.size -= 1
        if self.size > 0:
            self.head.prev = None
        return value
