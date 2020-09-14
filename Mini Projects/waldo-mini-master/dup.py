from typing import List


def every_column_dups(m: List[List[int]]) -> bool:
    """Returns True iff every column has at least one duplicate element.
    Examples:
    every_column_dups([[0, 1, 2],
                        [0, 2, 3],
                        [4, 2, 3]]) == True
    every_column_dups([[0, 1, 2],
                        [1, 1, 2],
                        [2, 3, 3]]) == False (first column has no duplicates)
    every_column_dups([]) == True (vacuous case, no columnns)
    every_column_dups([[]]) == True (one row, no columns)
    """
    if len(m) == 0:
        return True
    has = set()
    for col_i in range(len(m[0])):
        has_dup = True
        for row_i in range(len(m)):
            if m[row_i][col_i] not in has:
                has.add(m[row_i][col_i])
                has_dup = False
        if not has_dup:
            return True
    return False

#print(every_column_dups([[0, 1, 2],
                       #[0, 2, 3],
                       #[4, 2, 3]]))
#print(every_column_dups([[0, 1, 2],
                       #[1, 1, 2],
                       #[2, 3, 3]]))

def in_order(l):
    if len(l) == 0:
        return True
    else:
        cur_item = l[0]
        for item in l:
            if item < cur_item:
                return False
            cur_item = item
        return True
#print(in_order([1, 2, 3, 4]))
#print(in_order([2, 1, 3, 2]))


def some_column_increasing(m: List[List[int]]) -> bool:
    """True if any column of m is non-decreasing.
    Example: [[5, 7, 3],
              [3, 7, 4],
              [8, 8, 3]]  -> True because 7, 7, 8 is an increasing sequence
    Example: [[5, 7, 3],
              [3, 7, 4],
              [8, 6, 3]] -> False, no column is increasing
    Example:  [] -> False  (no columns, so none are increasing)
    Example:  [[]] -> False (no columns, so none are increasing)
    Example:  [[42]] -> True  single value is an increasing sequence
    """
    if len(m) == 0:
        return False
    for col_i in range(len(m)):
        is_sorted = True
        for row_i in range(len(m[col_i])):
            cur_item = m[row_i][0]
            item = m[row_i][col_i]
            if item < cur_item:
                is_sorted = False
            item = cur_item


print(some_column_increasing([[5, 7, 3], [3, 7, 4], [8, 8, 3]]))
print(some_column_increasing([[5, 7, 3], [5, 7, 4], [8, 6, 3]]))