#Subject: Given star coordinates (row, col) and a grid size,
#return a list of strings drawing the grid — * where a star sits,
#. elsewhere. Out-of-bounds coordinates are ignored.

def constellation_mapper(stars: list[tuple[int, int]], size: int) -> list[str]:
    grid = [["."] * size for _ in range(size)]
    for r, c in stars:
        if 0 <= r < size and 0 <= c < size:
            grid[r][c] = "*"
    return ["".join(row) for row in grid]

print(constellation_mapper([(0, 0), (1, 1), (2, 2)], 3)) #['*..', '.*.', '..*']
print(constellation_mapper([(1, 1), (0, 1), (2, 1), (1, 0), (1, 2)], 3)) #['.*.', '***', '.*.']
print(constellation_mapper([], 2)) #['..', '..']
print(constellation_mapper([(0, 1), (1, 1), (2, 1)], 3)) #['.*.', '.*.', '.*.']
print(constellation_mapper([(0, 0), (5, 5)], 6)) #['*..', '...', '...']
