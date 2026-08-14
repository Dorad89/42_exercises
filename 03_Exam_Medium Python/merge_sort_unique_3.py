#Subject: Given a list of lists,
#merge all elements into a single sorted list with duplicates removed.

def merge_sort_unique(lists: list[list[int]]) -> list[int]:
    merged = set()
    for lst in lists:
        merged.update(lst)
    return sorted(merged)

# print(merge_sort_unique([[1, 3, 5], [2, 3, 6], [1, 7]]))