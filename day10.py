from collections.abc import Iterator
with open("input/input10.txt") as f:
# with open("sample/sample10.txt") as f:
    input_lines = f.read().strip().splitlines()
GRID = {complex(i,j): int(c) for i, row in enumerate(input_lines) for j,c in enumerate(row)}
starts=[xy for xy,c in GRID.items() if c == 0]
DIRECTIONS = (1, 1j, -1, -1j)

print(GRID)
print(starts)
print(DIRECTIONS)

def next_valid_step(xy: complex,slope: int) -> Iterator[complex]:
    for step in DIRECTIONS:
        if xy+step in GRID and GRID[xy+step]-slope == 1:
            yield xy+step

def peaks(xy: complex,slope: int) -> set[complex]:
    if GRID[xy] == 9:
        return {xy}
    return set().union(*(peaks(next_xy,slope+1) for next_xy in next_valid_step(xy,slope)))

def routes(xy: complex,slope: int) -> int:
    if GRID[xy]==9:
        return 1
    return sum(routes(next_xy,slope+1) for next_xy in next_valid_step(xy,slope))

print("Sol1:",sum(len(peaks(start,slope=0)) for start in starts))
print("Sol2:",sum(routes(start,slope=0) for start in starts))