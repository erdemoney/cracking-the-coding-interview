import sys

# question:
#   Write an algorithm such that if an element in an MxN matrix is 0, its
#   entire row and column are set to 0.
#
# concept:
#   Record placement of each zero found in the matrix
#   Write zeros to the respective rows and columns

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

def zeroMatrix(matrix: list) -> list:
    zeros = []

    # find all zeros
    for i, row in enumerate(matrix):
        for j, num in enumerate(row):
            if num == '0':
                zeros.append((i,j))

    # insert zeros
    for zero in zeros:
        row = zero[0]
        col = zero[1]
        for i in range(len(matrix[row])):
            matrix[row][i] = '0'

        for i in range(len(matrix)):
            matrix[i][col] = '0'

    return matrix

def main() -> int:
    input_file = open(sys.argv[1], 'r')
    m = readMatrix(input_file)
    print('original matrix:')
    printMatrix(m)
    print('\nzero matrix:')
    printMatrix(zeroMatrix(m))
    return 0

sys.exit(main())
