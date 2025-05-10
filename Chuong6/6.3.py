from collections import deque

def count_BDN_less_than_N(N):
    queue = deque(["1"])
    count = 0
    
    while queue:
        num = queue.popleft()
        num_int = int(num)
        
        if num_int >= N:
            break
        
        count += 1
        
        # Thêm số tiếp theo vào hàng đợi (tạo số BDN mới)
        queue.append(num + "0")
        queue.append(num + "1")
    
    return count

# Đọc số lượng test case
T = int(input().strip())

results = []
for _ in range(T):
    N = int(input().strip())
    results.append(str(count_BDN_less_than_N(N)))

# In kết quả
print("\n".join(results))
