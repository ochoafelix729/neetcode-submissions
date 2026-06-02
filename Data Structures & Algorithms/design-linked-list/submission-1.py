class Node:
    def __init__(self, val: int):
        self.val = val
        self.prev = None
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def get(self, index: int) -> int:
        if not self.head: return -1
        i = 0
        ptr = self.head
        while ptr and i < index:
            ptr = ptr.next
            i += 1
        if i < index: return -1
        return ptr.val if ptr else -1

    def addAtHead(self, val: int) -> None:
        new_node = Node(val)
        if not self.head:
            self.head = self.tail = new_node
        elif not self.head.next:
            self.tail.prev = new_node
            new_node.next = self.head
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def addAtTail(self, val: int) -> None:
        new_node = Node(val)
        if not self.tail:
            self.tail = new_node
            self.head = new_node
        elif not self.tail.prev:
            self.head.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def addAtIndex(self, index: int, val: int) -> None:
        new_node = Node(val)
        if index == 0:
            if not self.head:
                self.head = self.tail = new_node
            else:
                new_node.next = self.head
                self.head.prev = new_node
                self.head = new_node
            return
        
        ptr = self.head
        i = 0
        while ptr and i < (index-1):
            ptr = ptr.next
            i += 1
        if not ptr: return

        temp = ptr.next
        ptr.next = new_node
        new_node.prev = ptr
        new_node.next = temp

        if temp:
            temp.prev = new_node
        else:
            self.tail = new_node

    def deleteAtIndex(self, index: int) -> None:
        if not self.head: return
        
        ptr = self.head
        i = 0
        while ptr and i < index:
            ptr = ptr.next
            i += 1
        if not ptr: return

        if ptr == self.head:
            self.head = ptr.next
            if self.head:
                self.head.prev = None
            else:
                self.tail = None

        elif ptr == self.tail:
            self.tail = ptr.prev
            if self.tail:
                self.tail.next = None
            else:
                self.head = None

        else:
            ptr.prev.next = ptr.next
            ptr.next.prev = ptr.prev
    
    def Log(self):
        if not self.head: return
        ptr = self.head
        while ptr:
            print(ptr.val, "->", end=" ")
            ptr = ptr.next
        
ll = MyLinkedList()
ll.addAtTail(1)
ll.addAtTail(2)
ll.addAtTail(3)
ll.addAtIndex(3,5)
ll.Log()


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)