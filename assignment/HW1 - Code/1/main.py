import bisect

MIN_MERGE = 32


def get_array():
    size = int(input())

    array = []
    for i in range(0, size):
        nelem = int(input())
        array.append(nelem)

    return array


# Tim sort
def calcMinRun(n):
    r = 0
    while n >= MIN_MERGE:
        r |= n & 1
        n >>= 1
    return n + r


def insertionSort(arr, left, right):
    for i in range(left + 1, right + 1):
        j = i
        while j > left and arr[j] < arr[j - 1]:
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            j -= 1


def merge(arr, l, m, r):
    len1, len2 = m - l + 1, r - m
    left, right = [], []
    for i in range(0, len1):
        left.append(arr[l + i])
    for i in range(0, len2):
        right.append(arr[m + 1 + i])

    i, j, k = 0, 0, l

    while i < len1 and j < len2:
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1

        else:
            arr[k] = right[j]
            j += 1

        k += 1

    while i < len1:
        arr[k] = left[i]
        k += 1
        i += 1

    while j < len2:
        arr[k] = right[j]
        k += 1
        j += 1


def timSort(arr):
    n = len(arr)
    minRun = calcMinRun(n)

    for start in range(0, n, minRun):
        end = min(start + minRun - 1, n - 1)
        insertionSort(arr, start, end)

    size = minRun
    while size < n:

        for left in range(0, n, 2 * size):

            mid = min(n - 1, left + size - 1)
            right = min((left + 2 * size - 1), (n - 1))

            if mid < right:
                merge(arr, left, mid, right)

        size = 2 * size


def count(x, Yarr, n, basecon):
    if x > 1:
        return n - bisect.bisect(Yarr, x) + base_conditions_count(x, basecon)

    if x == 1:
        return basecon[0]

    return 0


def base_conditions_count(x, base):
    _count = base[0] + base[1]

    if x == 2:
        _count -= base[3] + base[4]
    elif x == 3:
        _count += base[2]

    return _count


# Base conditions
def base_conditions(Yarr):
    arr = [0, 0, 0, 0, 0]

    for i in range(0, len(Yarr) - 1):
        if Yarr[i] >= 5:
            break
        else:
            arr[Yarr[i]] = arr[Yarr[i]] + 1

    return arr


def pairs_count(Xarr, Yarr, n):
    pairs = 0
    for x in Xarr:
        pairs += count(x, Yarr, n, base_conditions(Yarr))

    return pairs


if __name__ == '__main__':
    X = get_array()
    Y = get_array()

    # timSort(Y)
    Y.sort()
    _len = len(Y)

    print(pairs_count(X, Y, _len))
