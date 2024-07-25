#!/usr/bin/python3
'''0-pascal_triangle.py'''


def pascal_triangle(n):
    '''Return list of Pascal’s triangle of n'''
    if n <= 0:
        return []

    P = []

    for idx in range (n):
        row = [1] * (idx + 1)

        for ndx in range(1, idx):
            row[ndx] = P[idx - 1][ndx - 1] + P[idx - 1][ndx]
        P.append(row)

    return P
