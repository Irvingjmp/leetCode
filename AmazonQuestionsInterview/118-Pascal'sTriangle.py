def generate(numRows):
    triangle = []

    for i in range(numRows):
        # Initialize the current row with 1s
        row = [1] * (i + 1)      

        for j in range(1, i):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        
        triangle.append(row)

    return triangle
    
print(generate(5))