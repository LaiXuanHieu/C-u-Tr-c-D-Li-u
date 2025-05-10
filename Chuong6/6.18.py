from collections import deque

# Hàm xoay bên trái (ô 1, 2, 4, 5)
def rotate_left(state):
    return (state[3], state[0], state[2], state[4], state[1], state[5])

# Hàm xoay bên phải (ô 2, 3, 5, 6)
def rotate_right(state):
    return (state[0], state[4], state[1], state[3], state[5], state[2])

# BFS tìm số bước ít nhất để biến đổi trạng thái từ start -> target
def min_steps(start, target):
    if start == target:
        return 0  # Nếu trạng thái ban đầu đã là trạng thái đích

    queue = deque([(start, 0)])  # (trạng thái hiện tại, số bước)
    visited = set()
    visited.add(start)

    while queue:
        state, steps = queue.popleft()

        # Sinh hai trạng thái mới
        next_states = [rotate_left(state), rotate_right(state)]
        for next_state in next_states:
            if next_state == target:
                return steps + 1  # Nếu đến đích, trả về số bước

            if next_state not in visited:
                queue.append((next_state, steps + 1))
                visited.add(next_state)

    return -1  # Không thể xảy ra vì luôn có cách biến đổi

# Xử lý input/output
def main():
    T = int(input().strip())  # Số lượng test case
    results = []

    for _ in range(T):
        start = tuple(map(int, input().split()))  # Trạng thái ban đầu
        target = tuple(map(int, input().split()))  # Trạng thái đích
        results.append(str(min_steps(start, target)))

    print("\n".join(results))

if __name__ == "__main__":
    main()
