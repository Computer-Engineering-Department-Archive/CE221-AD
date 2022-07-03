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


def get_sum(BIT, index):
    sum = 0

    while index > 0:
        # Add current node's value to sum
        sum += BIT[index]
        # Update index to get parent
        index -= index & (-index)

    return sum


def update_BIT(BIT, n, index, val):
    while index <= n:
        # Update current node's value
        BIT[index] += val
        # Update index to get parent
        index += index & (-index)


def calculate_inversion(arr, n):
    inversion_count = 0

    max_element = max(arr)

    # create BIT with initialize elements as 0
    BIT = [0] * (max_element + 1)
    for i in range(n - 1, -1, -1):
        inversion_count += get_sum(BIT, arr[i] - 1)
        update_BIT(BIT, max_element, arr[i], 1)
    return inversion_count


if __name__ == '__main__':
    # Constant maximum number of errors
    # Input Array
    MAX_ERROR = int(input())
    BIT = get_array()

    result = calculate_inversion(BIT, len(BIT))

    if result >= MAX_ERROR:
        print("No")
    else:
        print("Yes")
