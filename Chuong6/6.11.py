from collections import deque

def shortest_path_in_3d_box(A, B, C, box_slices):
    directions = [(0, 1, 0), (0, -1, 0), (1, 0, 0), (-1, 0, 0), (0, 0, 1), (0, 0, -1)]
    start = None
    end = None
    
    # Find start ('S') and end ('E') positions
    for a in range(A):
        for b in range(B):
            for c in range(C):
                if box_slices[a][b][c] == 'S':
                    start = (a, b, c)
                elif box_slices[a][b][c] == 'E':
                    end = (a, b, c)
    
    if not start or not end:
        return -1
    
    queue = deque([(start[0], start[1], start[2], 0)])  # (a, b, c, distance)
    visited = [[[False] * C for _ in range(B)] for _ in range(A)]
    visited[start[0]][start[1]][start[2]] = True
    
    while queue:
        a, b, c, dist = queue.popleft()
        
        if (a, b, c) == end:
            return dist
        
        for da, db, dc in directions:
            na, nb, nc = a + da, b + db, c + dc
            if 0 <= na < A and 0 <= nb < B and 0 <= nc < C:
                if not visited[na][nb][nc] and box_slices[na][nb][nc] != '#':
                    visited[na][nb][nc] = True
                    queue.append((na, nb, nc, dist + 1))
    
    return -1  # No path found

# Reading input and processing each test case
T = int(input().strip())
results = []

for _ in range(T):
    A, B, C = map(int, input().strip().split())
    box_slices = []
    
    for _ in range(A):
        slice = []
        for _ in range(B):
            slice.append(input().strip())
        box_slices.append(slice)
        if _ < A - 1:  # Skip the empty line after each slice except the last one
            input()
    
    result = shortest_path_in_3d_box(A, B, C, box_slices)
    results.append(result)

# Print results for each test case
for result in results:
    print(result)
