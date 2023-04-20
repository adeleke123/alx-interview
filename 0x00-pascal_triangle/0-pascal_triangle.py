#!/usr/bin/python3

def pascal_triangle(n):
    '''
    Returns a list of lists representing Pascal's triangle of n.
    Returns an empty list if n <= 0.
    '''
    if n <= 0:
        return []

    triangle = []
    prev_row = []
    for i in range(1, n + 1):
        row = []
        for j in range(i):
            if j == 0 or j == i - 1:
                row.append(1)  # First and last element of each row is always 1
            else:
                row.append(prev_row[j-1] + prev_row[j])  # Calculate element based on previous row
        prev_row = row
        triangle.append(row)
    return triangle
