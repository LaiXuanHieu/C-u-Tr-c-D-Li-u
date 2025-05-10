from collections import deque

def find_smallest_multiple(N):
    # Nếu N = 1 thì số nhỏ nhất là 9
    if N == 1:
        return 9

    queue = deque(["9"])
    visited = set()
    
    while queue:
        num = queue.popleft()
        num_int = int(num)
        
        # Nếu tìm được số chia hết cho N, trả về kết quả
        if num_int % N == 0:
            return num_int
        
        # Thêm vào hàng đợi số mới với chữ số 0 và 9
        for next_digit in ["0", "9"]:
            new_num = num + next_digit
            if new_num not in visited:
                queue.append(new_num)
                visited.add(new_num)

# Đọc số lượng test case
T = int(input().strip())

results = []
for _ in range(T):
    N = int(input().strip())
    results.append(str(find_smallest_multiple(N)))

# In kết quả
print("\n".join(results))
