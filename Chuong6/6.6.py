from collections import deque
import math

def min_operations(N):
    if N == 1:
        return 0

    queue = deque([(N, 0)])  # (Giá trị hiện tại, số bước)
    visited = set([N])  # Đánh dấu các số đã duyệt

    while queue:
        value, steps = queue.popleft()
        
        # Nếu đạt được 1, trả về số bước
        if value == 1:
            return steps

        # Thao tác (a): Giảm 1
        if (value - 1) not in visited:
            queue.append((value - 1, steps + 1))
            visited.add(value - 1)

        # Thao tác (b): Lấy max(u, v) nếu u * v = value
        for i in range(2, int(math.sqrt(value)) + 1):
            if value % i == 0:
                max_factor = max(i, value // i)
                if max_factor not in visited:
                    queue.append((max_factor, steps + 1))
                    visited.add(max_factor)
    
    return -1  # Trường hợp không thể (không xảy ra)

# Đọc dữ liệu từ input
T = int(input().strip())
results = []

for _ in range(T):
    N = int(input().strip())
    results.append(str(min_operations(N)))

# In kết quả mỗi test trên một dòng
print("\n".join(results))
