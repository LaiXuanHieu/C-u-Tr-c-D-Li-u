from collections import deque

def min_days_to_grow(R, C, grid):
    queue = deque()
    total_seeds = 0  # Tổng số hạt mầm cần nảy
    days = 0

    # Hướng di chuyển: trái, phải, trên, dưới
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # Tìm tất cả các cây non ban đầu và tổng số hạt mầm cần nảy
    for i in range(R):
        for j in range(C):
            if grid[i][j] == 2:
                queue.append((i, j, 0))  # (hàng, cột, số ngày)
            elif grid[i][j] == 1:
                total_seeds += 1

    # Nếu không có hạt nào cần nảy, trả về 0 ngày
    if total_seeds == 0:
        return 0

    # BFS để lan chất dinh dưỡng
    while queue:
        x, y, day = queue.popleft()
        days = max(days, day)

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < R and 0 <= ny < C and grid[nx][ny] == 1:
                grid[nx][ny] = 2  # Biến thành cây non
                queue.append((nx, ny, day + 1))
                total_seeds -= 1  # Giảm số hạt mầm cần nảy

    # Nếu vẫn còn hạt chưa nảy, trả về -1
    return -1 if total_seeds > 0 else days

def solve():
    T = int(input())  # Số test case
    for _ in range(T):
        R, C = map(int, input().split())  # Kích thước lưới
        grid = [list(map(int, input().split())) for _ in range(R)]  # Nhập lưới
        print(min_days_to_grow(R, C, grid))

# Chạy chương trình
solve()
