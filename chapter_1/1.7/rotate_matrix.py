import sys
import math

# question:
#   given an image represented by an NxN matrix, where each pixel in the image
#   is 4 bytes, write a method to rotate the image by 90 degrees.
#   Can you do this in place?
#
# concept:
#   transpose matrix
#   invert rows

def readMatrix(input_file) -> list:
    sz = input_file.readline().split()
    num_row = sz[0]
    num_col = sz[1]

    matrix = []
    for _ in range(int(num_row)):
        row = input_file.readline().split()
        assert len(row) == int(num_col)
        matrix.append(row)
    return matrix

def printMatrix(matrix: list):
    for row in matrix:
        print(' '.join(row))

def rotateMatrix(matrix: list) -> list:
    num_rows = len(matrix)
    num_cols = len(matrix[0])

    # invert cols
    matrix.reverse()

    # transpose
    for r in range(num_rows):
        for c in range(r, num_cols):
            matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]

    return matrix


def main() -> int:
    input_file = open(sys.argv[1], 'r')
    m = readMatrix(input_file)
    print('original matrix:')
    printMatrix(m)
    print('\nrotated matrix:')
    printMatrix(rotateMatrix(m))
    return 0

sys.exit(main())
