def selection_sort(A):
    n = len(A)
    for i in range(n-1):
        least = i
        for j in range(i+1,n):
            if (A[j]<A[least]):
                least = j
        
        A[i],A[least] = A[least],A[i]
def insertion_sort(A):
    n = len(A)
    for i in range(1,n):
        key = A[i]
        j = i-1
        while j>=0 and A[j] > key:
            A[j+1] = A[j]
            j -= 1
        A[j+1] = key