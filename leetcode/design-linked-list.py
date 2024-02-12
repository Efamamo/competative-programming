class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.head = None
        
    def get(self, index: int) -> int:
        i = 0
        current = self.head
        while current:
            if i == index:
                return current.val
            i +=1
            current = current.next
        return -1
        
    def addAtHead(self, val: int) -> None:
        node = Node(val)
        if not self.head:
            self.head = node
        else:
            node.next = self.head
            self.head = node
        

    def addAtTail(self, val: int) -> None:
        new_node = Node(val)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def addAtIndex(self, index: int, val: int) -> None:
        i=0
        node = Node(val)
        if index == 0:
            self.addAtHead(val)
        else:
            current = self.head
            while current:
                if index == i+1:
                    node.next = current.next
                    current.next = node
                    break
                i+=1
                current = current.next

    def deleteAtIndex(self, index: int) -> None:
        i=0
        if index == 0 and not self.head:
            return
        elif index == 0 and self.head:
            self.head = self.head.next
        
        else:
            prev = None
            current = self.head
            while current and i<index:
                if index == i:
                    break
                i+=1
                prev = current
                current = current.next
            if current:
                prev.next = current.next
    

        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)