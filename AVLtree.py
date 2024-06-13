class AVLNode:
    def __init__(self, key, height = 1, left=None, right=None):
        self.key = key
        self.height = height
        self.left =left
        self.right = right
        
class AVLTree:
    def __init__(self):
        self.root = None
    def height(self,node):
        if not node:
            return 0
        return node.height
    def update_height(self,node):
        node.height = max(self.height(node.left), self.height(node.right)) + 1
        
    def balance_factor(self, node):
        if not node:
            return 0
        return self.height(node.left) - self.height(node.right)
    def rotate_right(self,n):
        x = n.left
        T2 = x.right
        x.right = n
        n.left = T2
        self.update_height(n)
        self.update_height(x)
        
        return x
    def rotate_left(self, n):
        x = n.right
        T2 = x.left
        x.left = n
        n.right = T2
        self.update_height(n)
        self.update_height(x)
        
        return x
    def rebalance(self, node):
        self.update_height(node)
        balance = self.balance_factor(node)
        if balance > 1:
            if self.balance_factor(node.left) < 0:
                node.left = self.rotate_left(node.left)
            return self.rotate_right(node)
        
        if balance < -1:
            if self.balance_factor(node.right) > 0:
                node.right = self.rotate_right(node.right)
            return self.rotate_left(node)
        return node
    def _insert(self, node, key):
        if not node:
            return AVLNode(key)
        elif key < node.key:
            node.left = self._insert(node.left, key)
        else:
            node.right = self._insert(node.right, key)
        return self.rebalance(node)
    def insert(self, key):
        self.root = self._insert(self.root, key)
    
    def min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current
    def _delete(self, node, key):
        if not node:
            return node
        elif key < node.key:
            node.left = self._delete(node.left, key)
        elif key > node.key:
            node.right = self._delete(node.right, key)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            
            temp = self.min_value_node(node.right)
            node.key = temp.key
            node.right = self._delete(node.right, temp.key)
        return self.rebalance(node)
    
    def delete(self, key):
        self.root = self._delete(self.root, key)
        
    def preorder(self, n):
        print(str(n.key), end = " ")
        if n.left:
            self.preorder(n.left)
        if n.right:
            self.preorder(n.right)
    
    def inorder(self , n):
        if n.left:
            self.inorder(n.left)
        print(str(n.key), end = " ")
        if n.right:
            self.inorder(n.right)
    
    def postorder(self , n):
        if n.left:
            self.postorder(n.left)
        if n.right:
            self.postorder(n.right)
        print(str(n.key), end = " ")
        
aa = AVLTree()
aa.insert(10)
aa.insert(20)
aa.insert(30)
aa.insert(40)
aa.insert(50)
aa.insert(29)

aa.preorder(aa.root)
print()
aa.inorder(aa.root)
print()
aa.postorder(aa.root)
print()
        

# 연습장

def height(self,node):
    if not node:
        return 0
    return node.height
def update_height(self,node):
    node.height = max(self.height(node.left),self.height(node.right)) + 1
def balance_factor(self,node):
    if not node:
        return 0    
    return self.height(node.left) - self.height(node.right)

def rotate_right(self,node):
     x = node.left
     T2 = x.right
     x.right = node
     node.left = T2
     self.update_height(node)
     self.update_height(x)
     return x
def rotate_left(self, node):
    x = node.right
    T2  = x.left
    x.left = node
    node.right = T2
    self.update_height(node)
    self.update_height(x)
    return x
def rebalance(self, node):
    self.update_height(node)
    balance = self.balance_factor(self, node)
    if balance > 1:
        if self.balance_factor(node.left) < 0:
            node.left = self.rotate_left(node.left)
        return self.rotate_right(node)
    if balance < -1 :
        if self.balance_factor(node.right) < 0:
            node.right = self.rotate_right(node.right)
        return self.rotate_left(node)
    return node

def _insert(self,node,key):
    if not node:
        return AVLNode(key)
    elif key < node.key:
        node.left = self._insert(node.left,key)
    else:
        node.right = self._insert(node.right, key)
    return self.rebalance(node)

def insert(self,node,key):
    self.root = self._insert(self.root, key)
    
def min_value_node(self,node):
    current = node
    while current.left is not None:
        current = current.left
    return current

def _delete(self,node,key):
    if not node:
        return node
    elif key < node.key:
        node.left = self._delete(node.left, key)            
    elif key > node.key:
        node.right = self._delete(node.right, key)
    else:
        if node.left is None:
            return node.right
        if node.right is None:
            return node.left
        
        temp = self.min_value_node(node.right)
        node.key = temp.key
        node.right = self._delete(node.right, temp.key)
    
    return self.rebalance(node)

def delete(self,node,key):
    self.root = self._delete(self.root, key)    

# 연습장

class AVLTree:
    def __init__(self):
        self.root = None
    def height(self,node):
        if not node:
            return 0
        return node.height
    def update_height(self,node):
        node.height = max(self.height(node.left), self.height(node.right)) + 1
    def balance_factor(self,node):
        if not node:
            return 0
        return self.height(node.left) - self.height(node.right)
    
    def rotate_right(self,node):
        x = node.left
        T2 = x.right
        x.right = node
        node.left = T2
        self.update_height(x)
        self.update_height(node)
        return node
    def rotate_left(self,node):
        x = node.right
        T2 = x.left
        x.left = node
        node.right = T2
        self.update_height(x)
        self.update_height(node)
    def rebalance(self,node):
        self.update_height(node)
        balance = self.balance_factor(node)
        if balance > 1:
            if self.balance_factor(node.left) <=  0:
                node.left = self.rotate_left(node.left)
            return self.rotate_right(node)
        if balance < -1:
            if self.balance_factor(node.rigt)  > 0:
                node.right = self.rotate_right(node.right)
            return self.rotate_left(node)
                
        return node
    def _insert(self,node,key):
        if not node:
            return AVLNode(key)
        elif key < node.key:
            node.left = self._insert(node.left)
        else:
            node.right = self._insert(node.right)
        return self.rebalance(node)
    def insert(self,key):
        self.root = self._insert(self.root,key)
    def min_value_node(self,node):
        current = node
        while not current.left is None:
            current = current.left
        return current
    def _delete(self,node,key):
        if not node:
            return node
        elif key < node.key:
            node.left = self._delete(node.left)
        elif key > node.key:
            node.right = self._delete(node.right)
        else:
            temp = self.min_value_node(node.right)
            node.key = temp.key
            node.right = self._delete(node.right,temp.key)
        return self.rebalance(node)
    def delete(self,key):
        self.root = self._delete(self.root,key)


class AVLTree:
    def __init__(self):
        self.root = None
    def height(self,node):
        if not node:
            return  0 
        return node.height
    def update_height(self,node):
        node.height = max(self.height(node.left),self.height(node.right )) + 1
    def balance_factor(self,node):
        if not node:
            return 0
        return self.height(node.left) - self.height(node.right)
    def rotate_right(self,node):
        x = node.left
        T2 = x.right
        x.right = node
        node.left = T2
        self.update_height(x)
        self.update_height(node)
        return x
    def rotate_left(self,node):
        x = node.right
        T2 = x.left
        x.left = node
        node.right = T2
        self.update_height(x)
        self.update_height(node)
        return x
    def rebalance(self,node):
        self.update_height(node)
        balance = self.balance_factor(node)
        if balance>1:
            if self.balance_factor(node.left) < 0 :
                node.left = self.rotate_left(node.left)
            return self.rotate_right(node)
        if balance < -1:
            if self.balance_factor(node.right) > 0:
                node.right = self.rotate_right(node.right)
            return self.rotate_left(node)
        return node
    def _insert(self,node,key):
        if not node:
            return AVLNode(key)
        elif key < node.key:
            node.left = self._insert(node.left)
        else:
            node.right = self._insert(node.right)
        return self.rebalance(node)
    def insert(self,key):
        self.root = self._insert(self.root,key)
    def min_value_node(self,node):
        current = node
        while not current.left is  None:
            current = current.left
        return current
    def _delete(self,node,key):
        if not node:
            return node
        elif key < node.key:
            node.left = self._delete(node.left)
        elif key > node.key:
            node.right = self._delete(node.right)
        else:
            temp = self.min_value_node(node.right)
            node.key = temp.key
            node.right = self._delete(node.right,temp.key)
        return self.rebalance(node)
    def delete(self,key):
        self.root = self._delete(self.root,key)
        