def spiralOrder(matrix):
    if not matrix:
        return []

    rowBegin = 0
    rowEnd = len(matrix) - 1
    colBegin = 0
    colEnd = len(matrix[0]) - 1

    result = []

    while rowBegin <= rowEnd and colBegin <= colEnd:

        for j in range(colBegin, colEnd + 1):
            result.append(matrix[rowBegin][j])
        rowBegin += 1

        for i in range(rowBegin, rowEnd + 1):
            result.append(matrix[i][colEnd])
        colEnd -= 1

        if rowBegin <= rowEnd:
            for j in range(colEnd, colBegin - 1, -1):
                result.append(matrix[rowEnd][j])
            rowEnd -= 1

        if colBegin <= colEnd:
            for i in range(rowEnd, rowBegin - 1, -1):
                result.append(matrix[i][colBegin])
            colBegin += 1

    return result
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(spiralOrder(matrix))