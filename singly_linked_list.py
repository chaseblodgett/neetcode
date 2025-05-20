class Node:
    def __init__(self, val, next=None):
        self.next = None
        self.data = val

class LinkedList:

    def __init__(self):
        self.head = Node(-1)
        self.tail = self.head
        self.length = 0
    
    def get(self, index: int) -> int:
        
        curr = self.head.next
        i = 0
        while curr:
            if index == i:
                return curr.data
            curr = curr.next
            i += 1
        return -1

    def insertHead(self, val: int) -> None:
        new_head = Node(val)
        new_head.next = self.head.next
        self.head.next = new_head
        if not new_head.next:
            self.tail = new_head

    def insertTail(self, val: int) -> None:
        self.tail.next = Node(val)
        self.tail = self.tail.next

    def remove(self, index: int) -> bool:
        
        curr = self.head
        i = 0
        while curr and i < index:
            i+= 1
            curr = curr.next
        
        if curr and curr.next:
            if curr.next == self.tail:
                self.tail = curr
            curr.next = curr.next.next
            return True
        
        return False


    def getValues(self) -> List[int]:
        ret = []
        curr = self.head.next
        while curr:
            ret.append(curr.data)
            curr = curr.next
        return ret
    