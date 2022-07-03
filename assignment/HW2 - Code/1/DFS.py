import sys


def dp():
    init_val = sys.maxsize
    dist = [[init_val for x in range(N)] for y in range(M)]

    # initialize first row for next steps
    x, y = 0, 0
    for z in range(0, N):
        dist[x][z] = min(dist[x][z], min(abs(y - z), N - abs(y - z)))

    # calculate other rows based on previous rows
    for x in range(1, M):
        for y in range(0, N):
            for z in range(0, N):
                if word[x] == interpreter[z]:
                    direction = min(abs(y - z), N - abs(y - z))  # clockwise or anticlockwise
                    dist[x][y] = min(dist[x][y], dist[x - 1][z] + direction)

    return min(dist[-1]) + M


def dfs(k, i):
    if k == M:
        return 0

    # seriously this took me so long to debug. please dont ask me what the fuck it does.
    res = []
    for j in index_dict[word[k]]:
        res.append(cost(i, j) + dfs(k + 1, j) + 1)

    return min(res)


def cost(i, j):
    if j < i:
        return cost(j, i)

    return min(j - i, i + N - j)


if __name__ == "__main__":
    interpreter = list(input())
    word = list(input())
    M, N = len(word), len(interpreter)

    index_dict = {}
    for k, v in enumerate(interpreter):
        if v in index_dict:
            index_list = index_dict[v]
            index_list.append(k)
            index_dict[v] = index_list
        else:
            index_dict[v] = [k]

    k, i = 0, 0
    print(dfs(k, i))
