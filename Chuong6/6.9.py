from collections import deque

def bfs_min_steps(grid, N, start, end):
    """Sử dụng BFS để tìm số bước ít nhất từ start đến end."""
    a, b = start
    c, d = end
    
    # Hướng di chuyển: trái, phải, lên, xuống
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # BFS queue: Lưu vị trí hiện tại và số bước
    queue = deque([(a, b, 0)])
    
    # Mảng đánh dấu đã thăm
    visited = [[False] * N for _ in range(N)]
    visited[a][b] = True

    while queue:
        x, y, steps = queue.popleft()

        # Nếu đã đến đích, trả về số bước
        if (x, y) == (c, d):
            return steps

        # Duyệt theo 4 hướng
        for dx, dy in directions:
            nx, ny = x, y

            # Đi theo hướng hiện tại đến khi gặp vật cản hoặc ra khỏi lưới
            while 0 <= nx + dx < N and 0 <= ny + dy < N and grid[nx + dx][ny + dy] == '.':
                nx += dx
                ny += dy

            # Nếu điểm đến chưa thăm, thêm vào hàng đợi BFS
            if not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx, ny, steps + 1))

    return -1  # Nếu không tìm thấy đường đi (điều này không xảy ra theo đề bài)

def solve():
    # Đọc số lượng test cases
    T = int(input())
    
    for _ in range(T):
        # Đọc kích thước lưới
        N = int(input())
        
        # Đọc lưới
        grid = [list(input().strip()) for _ in range(N)]
        
        # Đọc điểm xuất phát (a, b) và điểm đích (c, d)
        a, b, c, d = map(int, input().split())
        
        # Gọi BFS để tìm số bước ít nhất
        print(bfs_min_steps(grid, N, (a, b), (c, d)))

# Chạy chương trình
solve()
