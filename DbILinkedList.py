import DNode
class DBILinkedList:
    def __init__(self):
        self.head =None
    def isEmpty(self):
        return self.head == None
    def isFull(self):
        return False
    def getNode(self,pos):
        if pos < 0:
            return None
        ptr = self.head
        for i in range(pos):
            if ptr == None:
                return None
            ptr = ptr.next
        return ptr
    def insert(self,pos,e):
        node = DNode(e,None)
        before = self.getNode(pos-1)
        if before == None:
            node.next = self.head
            self.head = node
        else:
            before.append(node)
    def delete(self,pos):
        before = self.getNode(pos-1)
        if before ==  None:
            before = self.head
            if self.head is not None:
                self.head = self.head.next
            return before
        else:
            return before.DNode.popNext()
    def size(self):
        ptr = self.head
        count = 0
        while ptr is not None:
            ptr = ptr.next
            count += 1
            
        return count  
          
        