import heapq
from sys import maxsize

N = 200
MAX_INT = maxsize
MIN_INT = -maxsize - 1


def min_dp(array, mem, size, dec, inc, idx):
    if idx == size:
        return 0

    if mem[dec][inc][idx] != -1:
        return mem[dec][inc][idx]

    if array[idx] < array[dec]:
        mem[dec][inc][idx] = min_dp(array, mem, size, idx, inc, idx + 1)

    if array[idx] > array[inc]:
        if mem[dec][inc][idx] == -1:
            mem[dec][inc][idx] = min_dp(array, mem, size, dec, idx, idx + 1)
        else:
            mem[dec][inc][idx] = min(min_dp(array, mem, size, dec, idx, idx + 1), mem[dec][inc][idx])

    if mem[dec][inc][idx] == -1:
        mem[dec][inc][idx] = 1 + min_dp(array, mem, size, dec, inc, idx + 1)
    else:
        mem[dec][inc][idx] = min(1 + min_dp(array, mem, size, dec, inc, idx + 1), mem[dec][inc][idx])

    return mem[dec][inc][idx]


# greedy approach for inc and dec subsets
def greedy(nums):
    total = sum(nums)

    length = len(nums)
    heap = [- nums[i] for i in range(length)]
    heapq.heapify(heap)

    subsets = 0
    ret = []
    while subsets <= total:
        current = -1 * heapq.heappop(heap)
        total -= current
        subsets += current
        ret.append(current)

    return ret


if __name__ == '__main__':
    results = []
    while True:
        arr_len = int(input())
        if arr_len == -1:
            break

        arr = [int(x) for x in input().split()]
        arr.append(MAX_INT)
        arr.append(MIN_INT)

        dp = []
        dps = arr_len + 2
        for i in range(dps):
            l1 = []
            for j in range(dps):
                l2 = []
                for k in range(dps):
                    l2.append(-1)
                l1.append(l2)
            dp.append(l1)

        result = min_dp(arr, dp, arr_len, arr_len + 1, arr_len, 0)
        results.append(result)

    for i in results:
        print(i)
