import pathlib
import sys

from collections import deque

def find_region(garden: list[str], x: int, y: int) -> tuple[int, int, set[tuple[int, int]]]:
  area, perimeter = 0, 0
  visited = {(x, y)}

  q = deque()
  q.append((x, y))

  while q:
    x, y = q.popleft()
    area += 1
    perimeter += sum((
      x == 0 or garden[y][x - 1] != garden[y][x],
      y == 0 or garden[y - 1][x] != garden[y][x],
      x + 1 == len(garden[y]) or garden[y][x + 1] != garden[y][x],
      y + 1 == len(garden) or garden[y + 1][x] != garden[y][x]
    ))

    for nx, ny in ((x - 1, y), (x, y - 1), (x + 1, y), (x, y + 1)):
      if not (0 <= nx < len(garden[0]) and 0 <= ny < len(garden)):
        continue
      if garden[ny][nx] != garden[y][x]:
        continue
      if (nx, ny) in visited:
        continue

      visited.add((nx, ny))
      q.append((nx, ny))

  return area, perimeter, visited

def count_sides(region: set[tuple[int, int]]) -> int:
  fences = set()
  sides = 0

  for (x, y) in sorted(region, key=lambda x: tuple(reversed(x))):
    for (ax, ay, side) in ((x - 1, y, 'L'), (x, y - 1, 'T'), (x + 1, y, 'R'), (x, y + 1, 'B')):
      if (ax, ay) not in region:
        dx, dy = int(ax == x), int(ay == y)
        if (x - dx, y - dy, side) not in fences and (x - dx, y - dy, side) not in fences:
          sides += 1
        fences.add((x, y, side))

  return sides

def fence_price(garden: list[str]) -> tuple[int, int]:
  visited = set()

  list_price, bulk_price = 0, 0

  for y, row in enumerate(garden):
    for x in range(len(row)):
      if (x, y) in visited:
        continue

      area, perimeter, region = find_region(garden, x, y)
      list_price += area * perimeter
      bulk_price += area * count_sides(region)
      visited |= region

  return list_price, bulk_price

def run() -> None:
    with open("input/input12.txt") as f:
    # with open("sample/sample12.txt") as f:
        garden = [line.strip() for line in f.readlines()]

    list_price, bulk_price = fence_price(garden)
    print(f"Total fence price: {list_price}")
    print(f"Total bulk fence price: {bulk_price}")

run()