#Subject: Given a list of lists, return the sorted,
#deduplicated numbers that appear in every list.

def list_intersection(lists: list[list[int]]) -> list[int]:
    if not lists:
        return []
    common = set()
    for lst in lists:
        common &= set(lst)
    return sorted(common)

# print(list_intersection([[5, 4, 3], [2, 1, 3], [2, 1, 3]]))
# print(list_intersection([[5, 4, 3], [5, 4, 6], [4, 0, 5]]))
