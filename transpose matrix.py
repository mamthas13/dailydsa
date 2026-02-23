from typing import List

class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        result = [[None for i in range(len(matrix))] 
                  for j in range(len(matrix[0]))]

        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                result[col][row] = matrix[row][col]

        return result


# Run the function
matrix = [
    [1, 2, 3],
    [4, 5, 6]
]

sol = Solution()
print(sol.transpose(matrix))