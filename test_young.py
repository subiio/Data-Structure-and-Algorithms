import ArrayQueue

class BTNode:
    def __init__(self,elem, left = None, right = None):
        self.data = elem
        self.left = left
        self.right = right
    
def preorder(n):
    if n is not None:
        print(n.data, end= ' ')
        preorder(n.left)
        preorder(n.right)
def inorder(n):
    if n is not None:
        inorder(n.left)
        print(n.data, end = ' ')
        inorder(n.right)
def postorder(n):
    if n is not None:
        postorder(n.left)
        postorder(n.right)
        print(n.data, end= ' ')
def level_order(n):
    level_queue = ArrayQueue(100)
    level_queue.enqueue(n)
    while not level_queue.isEmpty():
        x = level_queue.dequeue
        if not x == None:
            print(x.data, end = ' ')
            level_queue.enqueue(x.left)
            level_queue.enqueue(x.right)
def count_node(n):
    if n is None:
        return 0
    else:
        return count_node(n.left) + count_node(n.right) + 1
def calc_height(n) :
    if n is None:
        return 0
    hLeft = calc_height(n.left)
    hRight = calc_height(n.right)
    if (hLeft > hRight):
        return hLeft + 1
    else:
        return hRight + 1
        

# test program

d = BTNode('D', None, None)
e = BTNode('E', None, None)
b = BTNode('B', d, e)
f = BTNode('F', None, None)
c = BTNode('C', f, None)
root = BTNode('A',b,c)

print('\n In-Order :', end = ''); inorder(root)
print('\n Pre-Order :', end = ''); preorder(root)
print('\n Post-Order :', end = ''); postorder(root)
print('\n Level-Order :', end = ''); level_order(root)
print()

print(" 노드의 개수 = %d개" % count_node(root))
print(" 트리의 높이 = %d" % calc_height(root))


