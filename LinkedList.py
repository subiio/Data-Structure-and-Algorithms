from Node import Node
class LinkedList():
    def __init__(self):
        self.head = None
    #헤드는 연결리스트 시작 노드를 가리키는 헤더 포인터만 직접 관리
    def isEmpty():
        return self.head == None
    def isFull(self):
        return False
    def getNode(self,pos):
        if pos < 0: return None
        ptr = self.head
        for _ in range(pos):
            if ptr == None:
                return None
            ptr = ptr.link        
        return ptr
    def insert(self,pos,e):
        node = Node(e,None)
        before = self.getNode(pos-1)
        if before == None:
            node.link = self.head
            self.head = node
        else: before.append(node)
        
    
        
    def delete(self,pos):
        before = self.getNode(pos-1)
        if before == None:
            before = self.head
            if self.head is not None:
                self.head = self.head.link
            return before
        else:
            return before.popNext()
    def size(self):
        ptr = self.head
        count = 0
        while ptr is not None:
            ptr = ptr.link
            count += 1
        return count