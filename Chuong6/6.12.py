from collections import deque

def generate_loc_phat_numbers(N):
    queue = deque(["6", "8"])
    result = []
    
    while queue:
        num = queue.popleft()
        if len(num) > N:
            break
        result.append(num)
        queue.append(num + "6")
        queue.append(num + "8")
    
    return sorted(result, reverse=True)  # Sắp xếp giảm dần

# Đọc số lượng test cases
T = int(input().strip())
test_cases = [int(input().strip()) for _ in range(T)]

# Xử lý từng test case
for N in test_cases:
    print(" ".join(generate_loc_phat_numbers(N)))
