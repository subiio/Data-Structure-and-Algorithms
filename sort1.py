data = [6,3,7,4,9,1,5,2,8]
print("Original:",data)


def selection_sort(A):
    n = len(A)
    for i in range(n-1):
        least = i
        for j in range(i+1,n):
            if A[j] < A[least]:
                least = j
            
        A[i],A[least] = A[least],A[i]

def insertion_sort(A):
    n = len(A)
    for i in range(n):
        key = A[i]
        j = i -1
        while j >= 0 and A[j] >= key:
            A[j+1] = A[j]
            j -= 1
        
        A[j+1] = key

                                   
def shell_sort(A):
    n = len(A)
    gap = n//2
    while gap > 0:
        for i in range(gap,n):
            temp = A[i]
            j = i
            while j >= gap and A[j] >= temp:
                A[j] = A[j-gap]
                j -= gap
            A[j] = temp
        gap //= 2
        

def merge(left,right):
    result = []
    left_index, right_index = 0,0 
    
    while left_index <= len(left) and right_index <= len(right) :
        if left[left_index] <= right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1
    while left_index <= len(left):
        result.append(left_index)
        left_index += 1
    while right_index <= len(right):
        result.append(right_index)
        right_index += 1
        
def merge_sort(A):
    if len(A)<=1:
        return A
    mid = len(A)//2
    
    left_half = A[:mid]
    right_half = A[mid:]
    
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

def selection_sort(A):
    n =len(A)
    for i in range(n):
        least = i
        for j in range(i+1,n):
            if A[least] > A[j]:
                least= j
        A[i],A[least] = A[least], A[i]
def insertion_sort(A):
    n = len(A)
    for i in range(n):
        key = A[i]
        j = i-1
        while j>=0 and A[j] >= key:
            A[j+1] = A[j]
            j -= 1
        A[j+1] = key

def partition(A,left,right):
    pivot= A[left]
    low = left+1
    high =right
    
    while low <= high:
        while low <= right and A[low] <= pivot:
            low += 1
        while high >= left and A[high] > pivot:
            high -= 1
        if low <= high:
            A[low],A[high] = A[high],A[low]
    A[left],A[high] =A[high],A[left]
    
def quick_sort(A,left,right):
    if left <= right:
        q = partition(A,left,right)
        quick_sort(A,left,q-1)
        quick_sort(A,q+1,right)
        

def selection_sort(A):
    n = len(A)
    for i in range(n):
        least = i
        for j in range(i+1, n):
            if A[least] > A[j]:
                least = j
        A[least],A[i] = A[i], A[least]

def insertion_sort(A):
    n = len(A)
    for i in range(n):
        key = A[i]
        j = i-1
        while j >= 0 and A[j] >= key:
            A[j+1] = A[j]
            j -= 1
        
        A[j+1] = key

def shell_sort(A):
    n = len(A)
    gap = n //2 
    while gap > 0:
        for i in range(gap,n):
            temp = A[i]
            j = i
            while j >= gap and A[j] >= temp:
                A[j] = A[j-gap]
                j -= gap
            A[j] = temp
        gap //= 2

def merge(left,right):
    result = []
    left_index, right_index = 0,0
    while left_index <= len(left) and right_index <= len(right):
        if left[left_index] <= right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1
    
    while left_index <= len(left):
        result.append(left[left_index])
        left_index += 1
    while right_index <= len(right):
        result.append(right[right_index])
        right_index += 1
    
    return result

def merge_sort(A):
    if len(A)<=1:
        return A
    mid = len(A)//2
    left_half = A[:mid]
    right_half = A[mid:]
    
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)
    return merge(left_half,right_half)

def partition(A,left,right):
    pivot =left
    low = left + 1
    high = right
    
    while low <= high:
        while low <= right and A[low] <= pivot:
            low += 1
        while high >= left and A[high] > pivot:
            high -=1
        if low <= high:
            A[low],A[high] = A[high], A[low]
    
    A[left],A[high] = A[high], A[left]
    return high

def quick_sort(A,left,right):
    if left <= right:
        q= partition(A,left,right)
        quick_sort(A,left,q-1)
        quick_sort(A,q+1,right)


def selection_sort(A):
    n = len(A)
    for i in range(n):
        least = i
        for j in range(i+1,n):
            if A[least] > A[j]:
                least= j
        A[least],A[i] = A[i],A[least]
def insertion_sort(A):
    n = len(A)
    for i in range(n):
        key  =A[i]
        j = i-1
        while j >= 0 and A[j] >= key:
            A[j+1] = A[j]
            j -= 1
        A[j+1] = key
        
def shell_sort(A):
    n = len(A)
    gap = n//2
    while gap >0:
        for i in range(gap,n):
            temp = A[i]
            j = i
            while j >= gap and A[j] >= temp:
                A[j] = A[j-gap]
                j -= gap
            A[j] = temp
        gap //= 2

def merge(left,right):
    result = []
    left_index,right_index =0,0
    while left_index <= len(left) and right_index <= len(right):
        if left[left_index] <= right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1
    while left_index <= len(left):
        result.append(left[left_index])
        left_index += 1
    while right_index <= len(right):
        result.append(right[right_index])
        right_index += 1
    return result
def merge_sort(A):
    if len(A) <= 1:
        return A
    mid = len(A)//2
    left_half = A[:mid]
    right_half = A[mid:]
    
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)
    
    return merge(left_half,right_half)

def partition(A,left,right):
    pivot = left
    low = left + 1
    high = right
    while low <= high:
        while low <= right and A[low] <= pivot:
            low += 1
        while high >= left and A[high ]> pivot:
            high -= 1
        if low <= high:
            A[low],A[high] = A[high],A[low]
        A[left],A[high] = A[high], A[left]

def quick_sort(A,left,right):
    if left <= right:
        q = partition(A,left,right)
        quick_sort(A,left,q-1)
        quick_sort(A,q+1,right)


               
    