


def sequential_search(A, key, low,high):
    for i in range(low, high + 1):
        if A[i] == key:
            return i
        return -1
    
    
def binary_search(A, key, low, high):
    if (low <= high):
        middle = (low + high)//2
        if key == A[middle]:
            return middle
        elif (key<A[middle]):
            return binary_search(A,key,low, middle -1)
        else:
            return binary_search(A,key,middle+1,high)
    return -1
def binary_search_iter(A,key,low,high):
    while (low <= high):
        middle = (low+high)//2
        if key == A[middle]:
            return middle
        elif (key > A[middle]):
            low = middle +1
        else:
            high = middle -1
    return -1

def sequential_search(A,key,low,high):
    for i in range(low, high+ 1):
        if A[i] == key:
            return i
        return -1
def binary_search(A,key,low,high):
    if low <= high:
        middle = (low+high)//2
        if A[middle] == key:
            return middle
        elif A[middle] < key:
            return binary_search(A,key,middle+1,high)
        else:
            return binary_search(A,key,low, middle -1)
    return -1
          
class BSTNode:
    def __init__(self,key,value):
        self.key = key
        self.value = value
        self.left = None
        self.right =None
        

def search_bst(n,key):
    if n == None:
        return None
    elif key == n.key:
        return n
    elif key < n.key:
        return search_bst(n.left,key)
    else:
        return search_bst(n.right,key)
    
def search_bst(n,key):
    if n == None:
        return None
    elif key == n.key:
        return n
    elif key < n.key:
        return search_bst(n.left,key)
    else:
        return search_bst(n.right,key)
    
def delete_bst(root, key):
    if root == None:
        return root
    if key < root.key:
        root.left = delete_bst(root.left, key)
    elif key > root.key:
        root.right = delete_bst(root.right, key)
    
    else:
        if root.left == None:
            return root.right
        
        if root.right == None:
            return root.left
        
        succ = root.right
        while succ.left != None:
            succ = succ.left
        root.key = succ.key
        root.value = succ.value
        root.right = delete_bst(root.right, succ.key)
    return root    

        