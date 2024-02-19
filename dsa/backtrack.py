class Solution:
    def spiralOrder(self, matrix):
        result = []

        while matrix:
            # Traverse top row
            result += matrix.pop(0)
            print("Top Row:", result)

            if matrix and matrix[0]:
                # Traverse right column
                for row in matrix:
                    result.append(row.pop())
                print("Right Column:", result)

            if matrix:
                # Traverse bottom row
                result += matrix.pop()[::-1]
                print("Bottom Row:", result)

            print("hey",matrix)

            if matrix and matrix[0]:
                # Traverse left column
                for row in matrix[::-1]:
                    print("hey2",matrix)
                    result.append(row.pop(0))
                print("Left Column:", result)

        return result

# Example usage:
solution = Solution()
matrix = [
    [1,2,3,4,5],
    [6,7,8,9,10]
    
]
print(matrix[::-1])
print(solution.spiralOrder(matrix))  
