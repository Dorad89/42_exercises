#Subject: Given a list of lists, return the sorted,
#deduplicated numbers that appear in every list.


def list_intersection(lists: list[list[int]]) -> list[int]:
    if not lists:
        return []
    common = set(lists[0])
    for lst in lists[1:]:
        common &= set(lst)
    return sorted(common)

def list_intersection(lists: list[list[int]]) -> list[int]:
    if not lists:
        return []
    common = set(lists[0])
    for lst in lists[1:]:
        common &= set(lst)
        if not common:
            return []
    return sorted(common)

print(list_intersection([[5, 4, 3], [2, 1, 3], [2, 1, 3]]))
print(list_intersection([[5, 4, 3], [2, 1, 6], [7, 0, 9]]))
