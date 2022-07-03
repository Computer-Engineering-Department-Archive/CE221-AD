import bisect

"""
get_array() -> []

Create a new list from console
"""


def get_array():
    size = int(input())

    array = []
    for i in range(0, size):
        nelem = int(input())
        array.append(nelem)

    return array


def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[i] < arr[l]:
        largest = l

    if r < n and arr[largest] < arr[r]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]

        heapify(arr, n, largest)


def heapSort(arr):
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)


def partition(arr, low, high):
    i = (low - 1)
    pivot = arr[high]

    for j in range(low, high):

        if arr[j] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quickSort(arr, low, high):
    if len(arr) == 1:
        return arr
    if low < high:
        pi = partition(arr, low, high)

        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)


if __name__ == '__main__':
    # Constant maximum number of errors
    # Input Array
    MAX_ERROR = int(input())
    array = get_array()

    heap = []
    # Create a sorted version of input array
    for index, value in enumerate(array):
        # Sort array by pairs first value
        heap.append((value, index))

    # Sort heap
    quickSort(heap, 0, len(array) - 1)

    inversion_count = 0
    # Index array
    x = []
    while heap:
        value, index = heap.pop()
        # Determine index of index pre-append in a way x stay sorted
        loc = bisect.bisect(x, index)
        inversion_count += index - loc

        # Insert index but keep x sorted
        bisect.insort(x, index)

    if inversion_count > MAX_ERROR:
        print("No")
    else:
        print("Yes")
