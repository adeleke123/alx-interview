#!/usr/bin/python3
'''
Returns list representing the Pascal's triangle of n
'''


def pascal_triangle(n):
    '''returns empty list if n <= 0'''
    if n <= 0:
        return []

    triangle = []
    row = []
    prev_row = []
    for m in range(0, n + 1):
        row = [k > 0 and k < m - 1 and m > 2 and prev_row[k-1] +
               prev_row[k] or 1 for k in range(0, m)]
        prev_row = row
        triangle += [row]
    return triangle[1:]
