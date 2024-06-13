class Node:
    def __init__(self,data,link = None):
        super.__init__()
        self.data = data
        self.link = link
    def append(self,node):
        if node is not None:
            node.link = self.link 
            self.link = node
    def popNext(self):
        next = self.link
        if next is not None:
            self.link = next.link
        return next     

# self 이전 노드
# self.link 다음 노드
# append시 node.link가 self.link가 되고
# self.link가 = node가 된다.

#popNext시 지우는 다음단계 노드를 링크해야함
# next= self.link
# next가 None이 아니라면 
# self.link = next.link

    