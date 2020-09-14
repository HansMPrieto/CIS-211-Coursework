"""Hans Prieto
List Sweep Algorithms Mini-Project
"""

def all_same(l: list) -> bool:
    """Determines whether all the elements
    in a list are the same.
    """
    if len(l) == 0:
        return True
    else:
        first_item = l[0]
        for item in l:
            if item != first_item:
                return False
        return True

def max_run(l: list) -> int:
    """Determines the maximum sublist
    length in a given list.
    """
    if len(l) == 0:
        return 0
    else:
        grouped_items = []
        prev_item = l[0]
        l = l[1:]
        subgroup = [prev_item]
        for item in l:
            if item != prev_item:
                grouped_items.append(subgroup)
                subgroup = []
            subgroup.append(item)
            prev_item = item
        grouped_items.append(subgroup)
        return max(len(list) for list in grouped_items)

def dedup(l: list) -> list:
    """Returns a de-duplicated version of an
    input list.
    """
    if len(l) == 0:
        return l
    else:
        dedup_list = []
        prev_item = l[0]
        dedup_list.append(prev_item)
        for item in l:
            if item != prev_item:
                dedup_list.append(item)
                prev_item = item
        return dedup_list
