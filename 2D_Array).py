def searchMatrix(matrix, target):
    if not matrix or not matrix[0]:
        return False
    row, col = 0, len(matrix[0]) - 1
    while row < len(matrix) and col >= 0:
        if matrix[row][col] == target:
            return True
        elif matrix[row][col] > target:
            col -= 1
        else:
            row += 1
    return False

def input_matrix():
    rows = int(input("Enter the number of rows: "))
    matrix = []
    print("Enter the rows as comma-separated values:")
    for _ in range(rows):
        row = list(map(int, input().split(',')))
        matrix.append(row)
    return matrix

# Input matrix from user
print("Please input your 2D matrix:")
matrix = input_matrix()

# Input target value from user
target = int(input("Enter the target value: "))

# Search and output result
result = searchMatrix(matrix, target)
if result== True:
    print("Output:", result)
    print("Explanation: The target value",target,"is present in the given 2D matrix")
else:
  print("Output:", result)
  print("Explanation: The target value",target,"is not present in the given 2D matrix")