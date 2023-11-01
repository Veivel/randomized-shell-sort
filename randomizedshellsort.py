import random

COMPARE_EXCHANGE_REPS = 4

def swap(arr, i, j):
    '''
    menukar arr[i] dan arr[j] secara in-place
    '''
    arr[i], arr[j] = arr[j], arr[i]

def compare_swap(arr, i, j):
    '''
    melakukan perbandingan antara arr[i] dan arr[j],
    jika urutan mereka terbalik maka lakukan swap()
    '''
    if ((i < j and arr[i] > arr[j]) or (i > j and arr[i] < arr[j])):
        swap(arr, i, j)

def permute_random(arr):
    '''
    melakukan shuffling untuk array arr secara in-place
    '''
    for i in range(len(arr)):
        j = random.randint(i, len(arr) - 1)
        swap(arr, i, j)

def compare_regions(arr, s, t, offset):
    '''
    membandingkan dan menukar dua region yang ditandai oleh arr[s] dan arr[t]
    '''
    mate = list(range(offset))
    for _ in range(COMPARE_EXCHANGE_REPS):
        permute_random(mate)
        for i in range(offset):
            compare_swap(arr, s + i, t + mate[i])

def randomized_shell_sort(arr: list) -> None:
    '''
    asumsi: panjang arr adalah pangkat 2
    '''
    n = len(arr)
    offset = n // 2
    while offset > 0: # log n iterations
        for i in range(0, n - offset, offset):
            compare_regions(arr, i, i + offset, offset)
        for i in range(n - offset, offset - 1, -offset):
            compare_regions(arr, i - offset, i, offset)
        for i in range(0, n - 3 * offset, offset):
            compare_regions(arr, i, i + 3 * offset, offset)
        for i in range(0, n - 2 * offset, offset):
            compare_regions(arr, i, i + 2 * offset, offset)
        for i in range(0, n, 2 * offset):
            compare_regions(arr, i, i + offset, offset)
        for i in range(offset, n - offset, 2 * offset):
            compare_regions(arr, i, i + offset, offset)
        offset //= 2