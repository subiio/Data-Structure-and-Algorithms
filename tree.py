from ArrayQueue import ArrayQueue

class BTNode:
    def __init__(self,elem, left = None, right = None):
        self.data = elem
        self.left = left
        self.right = right


def isLeaf(node):
    return node.right == None and node.left == None
    
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
        x = level_queue.dequeue()
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
table = [('A','.-'), ('B','-...'),('C','-.-.'),('D','-..'),
         ('E','.'),('F','..-.'),('G','--.'),('H','....'),
         ('I','..'),('J','.---'),('K','-.-'),('L','.-..'),
         ('M','--'),('N', '-.'),('O','---'),('P','.--.'),
         ('Q','--.-'),('R','.-.'),('S','...'),('T','-'),
         ('U','..-'),('V','...-'),('W', '.--'), ('X','-..-'),
         ('Y','-.--'),('Z','--..')]


def encode(ch):
    idx = ord(ch)-ord('A')
    return table[idx][1]
def decode_simple(morse):
    for tp in table:
        if morse == tp[1]:
            return tp[0]
def decode(root,code):
    node = root
    for   c in code:
        if c == '.'  : node = node.left
        elif c == '-' : node = node.right
    return node.data

str = input("입력 문장:")
mlist = []
for ch in str:
    code = encode(ch)
    mlist.append(code)
print("Morse Code:", mlist)
print("Decoding:", end = '')
for code in mlist:
    ch = decode_simple(code)    
    print(ch, end = '')   
print()
        

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

# 수식 트리 계산

# def evaluate(node):
#     if node is None:
#         return 0
#     if node.data in '+-*/':  # 연산자인 경우
#         op1 = evaluate(node.left)
#         op2 = evaluate(node.right)
#         if node.data == '+': return op1 + op2
#         elif node.data == '-': return op1 - op2
#         elif node.data == '*': return op1 * op2
#         elif node.data == '/': return op1 / op2
#     else:
#         return node.data  # 피연산자인 경우 바로 값을 반환
def evaluate(node):
    if node is None:
        return 0
    elif isLeaf(node):
        return node.data
    else:
        op1 = evaluate(node.left)
        op2 = evaluate(node.right)
        if node.data == '+' : return op1 + op2
        elif node.data == '-' : return op1 - op2
        elif node.data == '*' : return op1 * op2
        elif node.data == '/' : return op1 / op2

def buildETree(expr):
    if len(expr) == 0:
        return None
    
    token = expr.pop()
    # print("token:",token)
    if token in "+-*/" :
        node = BTNode(token)
        # print("node:",node.data)
        # print("expr:",expr)
        node.right = buildETree(expr)
        # print("node.right:", node.right.data)
        node.left = buildETree(expr)
        # print("node_left:",node.left.data)
        return node
    else:
        return BTNode(float(token))
########################
        # 1 3 + 4 2 / *
        #      *
        #     / \
        #    +   /
        #   / \ / \
        #  1  3 4  2
#########################
str = input("입력(후위표기):")
expr = str.split()
print(expr)
print("토큰분리(expr):",expr)
root = buildETree(expr)
print("\n 전위순회:", end=''); preorder(root)
print("\n 중위순회:", end=''); inorder(root)
print("\n 후위순회:", end=''); postorder(root)
print("\n 계산결과:", evaluate(root))
