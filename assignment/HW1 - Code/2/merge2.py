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


def mergesort(A, aux, low, high):
    if high <= low:
        return 0

    mid = low + ((high - low) >> 1)
    inversion_count = 0

    inversion_count += mergesort(A, aux, low, mid)
    inversion_count += mergesort(A, aux, mid + 1, high)
    inversion_count += merge(A, aux, low, mid, high)

    return inversion_count


def merge(A, Acopy, low, mid, high):
    k, i, j, inversion_count = low, low, mid + 1, 0

    while i <= mid and j <= high:
        if A[i] <= A[j]:
            swap(A, Acopy, i, k)
            i = i + 1
        else:
            swap(A, Acopy, j, k)
            j = j + 1
            inversion_count += (mid - i + 1)

        k = k + 1

    while i <= mid:
        swap(A, Acopy, i, k)
        k = k + 1
        i = i + 1

    for i in range(low, high + 1):
        swap(Acopy, A, i, i)

    return inversion_count


def swap(A, Acopy, i, k):
    Acopy[k] = A[i]


if __name__ == '__main__':
    # Constant maximum number of errors
    # Input Array
    MAX_ERROR = int(input())
    A = get_array()
    Acopy = A.copy()

    result = mergesort(A, Acopy, 0, len(A) - 1)

    if result >= MAX_ERROR:
        print("No")
    else:
        print("Yes")
