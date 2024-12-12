from pprint import pprint

# with open("input/input12.txt") as f:
with open("sample/sample12.txt") as f:
    input_lines = f.read().strip().split()

def calculate_area_perimeter_cost(matrix):
    from collections import defaultdict
    
    # Initialize a dictionary to hold area, perimeter, and cost for each character
    results = defaultdict(lambda: {'area': 0, 'perimeter': 0, 'cost': 0})
    
    rows = len(matrix)
    cols = len(matrix[0])
    
    # Directions for adjacent cells (up, down, left, right)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # Set to track visited cells
    visited = set()
    
    def dfs(x, y, char):
        stack = [(x, y)]
        area_count = 0
        perimeter_count = 0
        
        while stack:
            cx, cy = stack.pop()
            if (cx, cy) in visited:
                continue
            
            visited.add((cx, cy))
            area_count += 1
            
            # Check neighbors
            for dx, dy in directions:
                nx, ny = cx + dx, cy + dy
                if nx < 0 or nx >= rows or ny < 0 or ny >= cols:
                    # Out of bounds contributes to perimeter
                    perimeter_count += 1
                elif matrix[nx][ny] == char:
                    # Same character; add to stack for further exploration
                    stack.append((nx, ny))
                else:
                    # Different character contributes to perimeter
                    perimeter_count += 1
        
        return area_count, perimeter_count
    
    for i in range(rows):
        for j in range(cols):
            char = matrix[i][j]
            if (i, j) not in visited:
                area, perimeter = dfs(i, j, char)
                results[char]['area'] += area
                results[char]['perimeter'] += perimeter
                results[char]['cost'] += area * perimeter  # Calculate cost

    return results

# Example usage
matrix = [
    ['A', 'A', 'A', 'A'],
    ['B', 'B', 'C', 'D'],
    ['B', 'B', 'C', 'C'],
    ['E', 'E', 'E', 'C']
]
matrix=[[val for val in line] for line in input_lines]

result = calculate_area_perimeter_cost(matrix=matrix)
# pprint(matrix)
# Print the results
# print(result)
# Print the results
total=0
for char, metrics in result.items():
    total+=metrics["cost"]
    print(f"Character: {char}, Area: {metrics['area']}, Perimeter: {metrics['perimeter']}, Cost: {metrics['cost']}")

print(f"Total cost: {total}")