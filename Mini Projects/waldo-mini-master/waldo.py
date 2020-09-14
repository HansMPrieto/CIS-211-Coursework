"""Hans Prieto
Where are the Waldos Mini Project
"""

from typing import List

Waldo = 'W'
Other = '.'


def all_row_exists_waldo(m: List[List[str]]):
    """For all rows in the matrix, Waldo is in some column."""
    for row in m:
        has_waldo = False
        for col in row:
            if col == Waldo:
                has_waldo = True
        if not has_waldo:
            return False
    return True


def all_col_exists_waldo(m: List[List[str]]):
    """For all columns in the matrix, Waldo is in some row."""
    if len(m) == 0:
        return True
    for col_i in range(len(m[0])):
        has_waldo = False
        for row_i in range(len(m)):
            value = m[row_i][col_i]
            if value == Waldo:
                has_waldo = True
        if not has_waldo:
            return False
    return True


def all_row_all_waldo(m: List[List[str]]):
    """For all rows in the matrix, Waldo is in every column."""
    for row in m:
        for col in row:
            if col != Waldo:
                return False
    return True


def all_col_all_waldo(m: List[List[str]]):
    """For all the columns in the matrix, Waldo is in every row."""
    if len(m) == 0:
        return True
    for col_i in range(len(m[0])):
        for row_i in range(len(m)):
            value = m[row_i][col_i]
            if value != Waldo:
                return False
    return True


def exists_row_all_waldo(m: List[List[str]]):
    """There is some row in the matrix in which Waldo is in every column."""
    for row in m:
        exists_all_waldo = True
        for col in row:
            if col != Waldo:
                exists_all_waldo = False
        if exists_all_waldo:
            return True
    return False


def exists_col_all_waldo(m: List[List[str]]):
    """There is some column in the matrix in which Waldo is in every row."""
    if len(m) == 0:
        return False
    for col_i in range(len(m[0])):
        all_waldo = True
        for row_i in range(len(m)):
            value = m[row_i][col_i]
            if value != Waldo:
                all_waldo = False
        if all_waldo:
            return True
    return False


def exists_row_exists_waldo(m: List[List[str]]):
    """There is some row in the matrix in which Waldo is in some column."""
    for row in m:
        for col in row:
            if col == Waldo:
                return True
    return False


def exists_col_exists_waldo(m: List[List[str]]):
    """There is some column in the matrix in which Waldo is in some row."""
    if len(m) == 0:
        return False
    for col_i in range(len(m[0])):
        for row_i in range(len(m)):
            value = m[row_i][col_i]
            if value == Waldo:
                return True
    return False
