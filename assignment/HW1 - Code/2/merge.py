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


def calculate_inversion(arr, n):
    # List with size of n
    temp_arr = [None] * n
    return merge_sort(arr, temp_arr, 0, n - 1)


def merge_sort(arr, temp_arr, left, right):
    inversion_count = 0

    if left < right:
        mid = (left + right) // 2

        inversion_count += merge_sort(arr, temp_arr, left, mid)
        inversion_count += merge_sort(arr, temp_arr, mid + 1, right)
        inversion_count += merge(arr, temp_arr, left, mid, right)

    return inversion_count


def merge(arr, temp_arr, left, mid, right):
    i, j, k, inversion_count = left, mid+1, left, 0

    while i <= mid and j <= right:

        if arr[i] <= arr[j]:
            swap(arr, i, k, temp_arr)
            k += 1
            i += 1
        else:
            swap(arr, j, k, temp_arr)
            inversion_count += (mid - i + 1)
            k += 1
            j += 1

    while i <= mid:
        swap(arr, i, k, temp_arr)
        k += 1
        i += 1

    while j <= right:
        swap(arr, j, k, temp_arr)
        k += 1
        j += 1

    for i in range(left, right + 1):
        swap(temp_arr, i, i, arr)

    return inversion_count


def swap(arr, i, k, temp_arr):
    temp_arr[k] = arr[i]


if __name__ == '__main__':
    # Constant maximum number of errors
    # Input Array
    MAX_ERROR = int(input())
    array = get_array()

    n = len(array)
    result = calculate_inversion(array, n)

    if result >= MAX_ERROR:
        print("No")
    else:
        print("Yes")
