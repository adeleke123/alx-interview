#!/usr/bin/python3

def pascal_triangle(n):
    """
    Generate Pascal's Triangle up to n rows.
    """
    if n <= 0:
        return []

    triangle = [[1]]  # Initialize with first row [1]

    # Generate subsequent rows based on previous row
    for i in range(1, n):
        row = [1]  # First element is always 1
        for j in range(1, i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])  # Calculate element based on previous row
        row.append(1)  # Last element is always 1
        triangle.append(row)

    return triangle
