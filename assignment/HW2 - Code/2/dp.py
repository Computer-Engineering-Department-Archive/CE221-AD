def filler(array, dp, n, i, j):
    if i < j:
        tmp = dp[0][j] + 1

        for k in range(1, i):
            if array[k] < array[i] and k != j:
                tmp = max(tmp, dp[k][j] + 1)

        return tmp

    else:
        tmp = dp[i][0] + 1
        for k in range(1, j):
            if arr[k] > arr[j] and k != i:
                tmp = max(tmp, dp[i][k] + 1)

        return tmp


def solve(array, n):
    dp = []
    for i in range(n+1):
        l1 = []
        for j in range(205):
            l1.append(-1)
        dp.append(l1)

    dp[0][0] = 0
    dp[1][0] = 1
    dp[0][1] = 1

    # print(dp)

    for i in range(2, n):
        for j in range(0, i):
            dp[i][j] = filler(arr, dp, n, i, j)
            dp[j][i] = filler(arr, dp, n, j, i)

    ans = 0
    for i in range(0, n):
        for j in range(0, n):
            if i != j:
                ans = max(ans, dp[i][j])

    print(ans)


if __name__ == "__main__":
    results = []
    # while int(input()) != -1:
    #     arr = list(map(int, input().split(" ", -1)))
    #     solve(arr, len(arr))

    while True:
        n = int(input())
        if n == -1:
            break

        arr = input().split(" ", -1)
        print(arr)

        solve(arr, n)
