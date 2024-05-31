#!/usr/bin/python3
"""The python enviorment"""


def pascal_triangle(n):
    """function that returns Pacals triangle"""
    if n <= 0:
        return [[]]
    result = [[1]]
    for i in range(n - 1):
        _space = [0] + result[-1] + [0]
        row = []
        for j in range(len(result[-1]) + 1):
            row.append(_space[j] + _space[j + 1])
        result.append(row)
    return result
