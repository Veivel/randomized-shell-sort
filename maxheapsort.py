def swap(arr, i, j):
    '''
    menukar arr[i] dan arr[j] secara in-place
    '''
    arr[i], arr[j] = arr[j], arr[i]

def heapify(arr, n, i):
    '''
    melakukan heapify A.K.A bubble_down, percolate_down
    kepada arr[i:]
    '''
    largest = i
    l, r = 2*i + 1, 2*i + 2 # children
    
    # ambil child terbesar
    if l < n and arr[i] < arr[l]:
        largest = l
    if r < n and arr[largest] < arr[r]:
        largest = r
        
    if largest != i:
        swap(arr, i, largest)
        heapify(arr, n, largest)
        
def heapsort(arr):
    '''
    Melakukan heapsort terhadap arr secara in-place
    '''
    n = len(arr)
    
    # convert arr menjadi max-heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
        
    # extract / sorting elemen satu per satu
    for i in range(n-1, 0, -1): 
        swap(arr, 0, i)
        heapify(arr, i, 0)