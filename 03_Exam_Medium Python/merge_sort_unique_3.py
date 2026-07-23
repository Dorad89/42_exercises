#Subject: Given a list of lists,
#merge all elements into a single sorted list with duplicates removed.

def merge_sort_unique(lists: list[list[int]]) -> list[int]:
    merged = set()
    for lst in lists:
        merged.update(lst)
    return sorted(merged)


def merge_sort_unique(lists):
    return sorted(set(x for y in lists for x in y))

lists = [[1, 3, 5], [2, 3, 6], [1, 7]]
print(merge_sort_unique(lists))