global heap_size
heap_size = 0

def LEFT(i):
    return 2 * i

def RIGHT(i):
    return 2 * i + 1

def PARENT(i):
    return i // 2

def max_heapify(A, i):
    global heap_size
    l = LEFT(i)
    r = RIGHT(i)

    if l < heap_size and A[l] > A[i]:
        largest = l
    else:
        largest = i

    if r < heap_size and A[r] > A[largest]:
        largest = r
    if not largest == i:
        A[i], A[largest] =  A[largest], A[i]
        max_heapify(A, largest)

def build_max_heap(A):
    global heap_size
    heap_size = len(A)
    for i in range(len(A) // 2, 1):
        max_heapify(A, i)


def HEAP_EXTRACT_MAX(A):
    heap_size = len(A)

    if heap_size < 1:
        print("error: heap empty")

    else:
        max = A[1]
        A[1] = A[heap_size-1]
        heap_size -= 1
        max_heapify(A, 1)
        return max

def HEAP_INCREASE_KEY(A, i, key):
    if key < A[i]:
        print("error: new key is smaller than current key")
    else:
        A[i] = key

    while i > 1 and A[PARENT(i)] < A[i]:
        A[i], A[PARENT(i)] = A[PARENT(i)], A[i]
        i = PARENT(i)

def MAX_HEAP_INSERT(A, key):
    i = len(A)

    i = i + 1

    A.append(float('-inf'))
    # A[len(A)] = float('-inf')

    print(A)
    HEAP_INCREASE_KEY(A, i, key)

def HEAP_DECREASE_KEY(A, i, key):
    if key > A[i]:
        print("error: new key is larger than current key")
    else:
        A[i] = key

    while i > 1 and A[PARENT(i)] > A[i]:
        A[i], A[PARENT(i)] = A[PARENT(i)], A[i]
        i = PARENT(i)

def MIN_HEAP_INSERT(A, key):
    i = len(A)

    i = i + 1

    A.append(float('inf'))
    # A[len(A)] = float('-inf')

    print(A)
    HEAP_DECREASE_KEY(A, i - 1, key)

def HEAP_EXTRACT_MIN(A):
    heap_size = len(A)

    if heap_size < 1:
        print("error: heap empty")

    else:
        min = A[1]
        A[1] = A[heap_size-1]
        heap_size -= 1
        min_heapify(A, 1)
        return min
    
def min_heapify(A, i):
    global heap_size
    l = LEFT(i)
    r = RIGHT(i)

    if l < heap_size and A[l] < A[i]:
        smallest = l
    else:
        smallest = i

    if r < heap_size and A[r] < A[smallest]:
        smallest = r
    if not smallest == i:
        A[i], A[smallest] =  A[smallest], A[i]
        min_heapify(A, smallest)

# A(1)=-10,

# A(2)=-8,

# A(3)=-9,

# A(4)=-7,

# A(5)=-7,

# A(6)=-6,

# A(7)=-6,

# A(8)=-4,

# A(9)=-4,

# A(10)=-5.

A = [-10, -8, -9, -7, -7, -6, -6, -4, -4, -5]

print(A)

MIN_HEAP_INSERT(A, -11)

print(A)