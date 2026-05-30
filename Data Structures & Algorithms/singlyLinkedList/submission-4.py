class Node:
    def __init__(self, val: int):
        self.val = val
        self.next = None


class LinkedList:
    
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def get(self, index: int) -> int:
        if self.head is None:
            return -1
        
        ptr = self.head
        i = 0
        while ptr and i < index:
            ptr = ptr.next
            i += 1

        if ptr is None:
            return -1
        return ptr.val        


    def insertHead(self, val: int) -> None:
        node = Node(val)

        if self.head is None:
            self.head = self.tail = node
        else:
            node.next = self.head
            self.head = node
        self.size += 1

    def insertTail(self, val: int) -> None:
        node = Node(val)

        if self.tail is None:
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.size += 1


    def remove(self, index: int) -> bool:
        if self.head is None or index >= self.size:
            return False
        
        if index == 0:
            if self.head.next:
                temp = self.head.next
                self.head.next = None
                self.head = temp
            else:
                self.head = None
            self.size -= 1
            return True
        
        ptr = self.head
        i = 0
        while ptr and i != (index-1):
            ptr = ptr.next
            i += 1
        
        if i < (index-1):
            return False

        if self.tail == ptr.next:
            ptr.next = None
            self.tail = ptr
        else:
            temp = ptr.next
            ptr.next = ptr.next.next
        self.size -= 1
        return True
        

    def getValues(self) -> List[int]:
        if self.head is None:
            return []
        
        values = []
        ptr = self.head
        while ptr:
            values.append(ptr.val)
            ptr = ptr.next
        return values

