from collections import deque

def min_steps_to_reach_end(matrix, M, N):
    # Hàng đợi BFS (chứa tọa độ (row, col) và số bước đi)
    queue = deque([(0, 0, 0)])  # (hàng, cột, số bước)
    visited = set()
    visited.add((0, 0))

    while queue:
        row, col, steps = queue.popleft()
        
        # Nếu đã đến đích, trả về số bước
        if row == M - 1 and col == N - 1:
            return steps
        
        jump = matrix[row][col]

        # Di chuyển sang phải
        new_col = col + jump
        if new_col < N and (row, new_col) not in visited:
            queue.append((row, new_col, steps + 1))
            visited.add((row, new_col))

        # Di chuyển xuống dưới
        new_row = row + jump
        if new_row < M and (new_row, col) not in visited:
            queue.append((new_row, col, steps + 1))
            visited.add((new_row, col))

    return -1  # Không tìm được đường đi

def main():
    T = int(input().strip())  # Số lượng test
    results = []
    
    for _ in range(T):
        M, N = map(int, input().strip().split())
        matrix = []
        
        for _ in range(M):
            matrix.append(list(map(int, input().strip().split())))

        results.append(str(min_steps_to_reach_end(matrix, M, N)))

    print("\n".join(results))

if __name__ == "__main__":
    main()
