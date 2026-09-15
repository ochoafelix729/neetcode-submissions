class Node:
    def __init__(self, key: int = 0, val: int = 0):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.cap = capacity
        self.size = 0
        self.cache = {} # key -> node -> value

    def get(self, key: int) -> int:
        if key in self.cache:
            self.updateMRU(key)
            return self.cache[key].val
        return -1

    def updateMRU(self, key: int) -> None:
        node = self.cache[key]
        node.prev.next = node.next
        node.next.prev = node.prev
        tmp = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = tmp
        tmp.prev = node

    def removeLRU(self) -> None:
        tmp = self.tail.prev.prev
        del self.cache[self.tail.prev.key]
        self.tail.prev.next = None
        self.tail.prev.prev = None
        tmp.next = self.tail
        self.tail.prev = tmp
        self.size -= 1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key].val = value
            self.updateMRU(key)
        else:
            node = Node(key, value)
            self.cache[key] = node
            tmp = self.head.next
            self.head.next = node
            node.next = tmp
            node.prev = self.head
            tmp.prev = node
            self.size += 1
            if self.size > self.cap:
                self.removeLRU()







