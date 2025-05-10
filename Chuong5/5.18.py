from collections import Counter

def nearest_greater_frequency(arr, n):
    # Bước 1: Đếm số lần xuất hiện của từng phần tử
    freq = Counter(arr)
    
    # Bước 2: Dùng stack để tìm phần tử gần nhất phía bên phải có số lần xuất hiện lớn hơn
    stack = []
    result = [-1] * n  # Mảng kết quả mặc định là -1
    
    for i in range(n - 1, -1, -1):
        # Loại bỏ các phần tử có số lần xuất hiện nhỏ hơn hoặc bằng arr[i]
        while stack and freq[arr[i]] >= freq[arr[stack[-1]]]:
            stack.pop()
        
        # Nếu stack không rỗng, phần tử trên đỉnh stack là kết quả cần tìm
        if stack:
            result[i] = arr[stack[-1]]
        
        # Đẩy chỉ mục hiện tại vào stack
        stack.append(i)
    
    return result

# Đọc input và xử lý từng test case
T = int(input().strip())

results = []
for _ in range(T):
    n = int(input().strip())
    if n == 0:
        results.append("")  # Nếu n = 0, không cần xử lý
        continue
    
    arr = list(map(int, input().strip().split()))
    results.append(" ".join(map(str, nearest_greater_frequency(arr, n))))

# Xuất kết quả
print("\n".join(results))
