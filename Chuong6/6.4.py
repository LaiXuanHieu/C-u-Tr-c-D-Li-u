from collections import deque

def find_smallest_BDN(N):
    queue = deque(["1"])  # Bắt đầu từ số 1
    
    while queue:
        num = queue.popleft()
        num_int = int(num)
        
        # Kiểm tra nếu num là bội số của N
        if num_int % N == 0:
            return num  # Trả về số BDN nhỏ nhất
        
        # Sinh số mới bằng cách thêm '0' và '1'
        queue.append(num + "0")
        queue.append(num + "1")

# Đọc số lượng test case
T = int(input().strip())

results = []
for _ in range(T):
    N = int(input().strip())
    results.append(find_smallest_BDN(N))

# In kết quả
print("\n".join(results))
