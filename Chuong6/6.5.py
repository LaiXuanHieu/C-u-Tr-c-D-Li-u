from collections import deque

def min_operations(S, T):
    if S >= T:
        return S - T  # Chỉ cần trừ đi 1 cho đến khi đạt T

    queue = deque([(S, 0)])  # (giá trị hiện tại, số bước)
    visited = set([S])

    while queue:
        value, steps = queue.popleft()
        
        # Nếu tìm thấy giá trị T
        if value == T:
            return steps
        
        # Thao tác (a): Giảm 1
        if value - 1 > 0 and (value - 1) not in visited:
            queue.append((value - 1, steps + 1))
            visited.add(value - 1)
        
        # Thao tác (b): Nhân đôi
        if value * 2 <= 20000 and (value * 2) not in visited:  # Giới hạn để tránh quá lớn
            queue.append((value * 2, steps + 1))
            visited.add(value * 2)

# Đọc dữ liệu từ input
T = int(input().strip())

results = []
for _ in range(T):
    S, T = map(int, input().strip().split())
    results.append(str(min_operations(S, T)))

# In kết quả mỗi test trên một dòng
print("\n".join(results))
