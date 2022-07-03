import sys
from enum import Enum


class Action(Enum):
    PRESS = 1
    RIGHT = 2
    LEFT = 3


if __name__ == '__main__':
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

    init_val = sys.maxsize
    dist = [[init_val for i in range(N)] for j in range(M)]

    i, j = 0, 0
    for k in range(0, N):
        dist[i][k] = min(dist[i][k], min(abs(j - k), N - abs(j - k)))

    for i in range(1, M):
        for j in range(0, N):
            for k in range(0, N):
                if word[i] == interpreter[k]:
                    dist[i][j] = min(dist[i][j], dist[i - 1][k] + min(abs(j - k), N - abs(j - k)))

    print(min(dist[-1]) + M)
