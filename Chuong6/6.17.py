from collections import deque

# Các nước đi hợp lệ của quân mã
KNIGHT_MOVES = [
    (2, 1), (2, -1), (-2, 1), (-2, -1),
    (1, 2), (1, -2), (-1, 2), (-1, -2)
]

# Chuyển vị trí dạng "a1" thành (row, col)
def chess_to_index(position):
    col = ord(position[0]) - ord('a')  # Chuyển 'a' -> 0, 'b' -> 1, ..., 'h' -> 7
    row = int(position[1]) - 1         # Chuyển '1' -> 0, '2' -> 1, ..., '8' -> 7
    return (row, col)

# BFS tìm số bước đi ngắn nhất
def min_knight_moves(start, end):
    if start == end:
        return 0  # Nếu đã ở vị trí cần đến

    queue = deque([(start[0], start[1], 0)])  # (row, col, steps)
    visited = set()
    visited.add(start)

    while queue:
        row, col, steps = queue.popleft()

        # Duyệt tất cả các nước đi hợp lệ của quân mã
        for dr, dc in KNIGHT_MOVES:
            new_row, new_col = row + dr, col + dc

            if 0 <= new_row < 8 and 0 <= new_col < 8:  # Kiểm tra nằm trong bàn cờ
                if (new_row, new_col) == end:
                    return steps + 1  # Nếu đến đích, trả về số bước

                if (new_row, new_col) not in visited:
                    queue.append((new_row, new_col, steps + 1))
                    visited.add((new_row, new_col))

    return -1  # Không thể xảy ra vì luôn có đường đi

# Xử lý input/output
def main():
    T = int(input().strip())  # Số lượng test case
    results = []
    
    for _ in range(T):
        start, end = input().strip().split()
        start_pos = chess_to_index(start)
        end_pos = chess_to_index(end)
        results.append(str(min_knight_moves(start_pos, end_pos)))

    print("\n".join(results))

if __name__ == "__main__":
    main()
