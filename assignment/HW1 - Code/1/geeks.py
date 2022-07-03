# Python3 program to find the number
# of pairs (x, y) in an array
# such that x^y > y^x
import bisect


# Function to return count of pairs
# with x as one element of the pair.
# It mainly looks for all values in Y
# where x ^ Y[i] > Y[i] ^ x


def count(x, Y, n, NoOfY):
    # If x is 0, then there cannot be
    # any value in Y such that
    # x^Y[i] > Y[i]^x
    if x == 0:
        return 0

    # If x is 1, then the number of pairs
    # is equal to number of zeroes in Y
    if x == 1:
        return NoOfY[0]

    # Find number of elements in Y[] with
    # values greater than x, bisect.bisect_right
    # gets address of first greater element
    # in Y[0..n-1]
    idx = bisect.bisect_right(Y, x)
    ans = n - idx
    ecount = 0

    # If we have reached here, then x must be greater than 1,
    # increase number of pairs for y=0 and y=1
    ecount += NoOfY[0] + NoOfY[1]

    # Decrease number of pairs
    # for x=2 and (y=4 or y=3)
    if x == 2:
        ecount -= NoOfY[3] + NoOfY[4]

    # Increase number of pairs
    # for x=3 and y=2
    if x == 3:
        ecount += NoOfY[2]

    print(ans, ecount)
    print(x, Y)
    return ans + ecount


# Function to return count of pairs (x, y)
# such that x belongs to X,
# y belongs to Y and x^y > y^x


def count_pairs(X, Y, m, n):
    # To store counts of 0, 1, 2, 3,
    # and 4 in array Y
    NoOfY = [0] * 5
    for i in range(n):
        if Y[i] < 5:
            NoOfY[Y[i]] += 1

    print(NoOfY)

    # Sort Y so that we can do binary search in it
    Y.sort()
    total_pairs = 0  # Initialize result

    # Take every element of X and
    # count pairs with it
    for x in X:
        total_pairs += count(x, Y, n, NoOfY)

    return total_pairs


# Driver Code
if __name__ == '__main__':
    X = [2, 6, 1]
    Y = [5, 1]
    print("Total pairs = ",
          count_pairs(X, Y, len(X), len(Y)))