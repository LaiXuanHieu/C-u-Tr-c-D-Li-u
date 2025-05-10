def stock_span(prices, n):
    stack = []  # Stack lưu chỉ mục của các ngày trước
    result = [0] * n  # Mảng kết quả

    for i in range(n):
        # Loại bỏ các phần tử có giá nhỏ hơn hoặc bằng giá ngày hiện tại
        while stack and prices[stack[-1]] <= prices[i]:
            stack.pop()
        
        # Nếu stack rỗng, nghĩa là từ đầu đến ngày hiện tại đều tăng
        if not stack:
            result[i] = i + 1
        else:
            result[i] = i - stack[-1]

        # Đẩy ngày hiện tại vào stack
        stack.append(i)

    return result

# Đọc input và xử lý từng test case
T = int(input().strip())

results = []
for _ in range(T):
    N = int(input().strip())
    prices = list(map(int, input().strip().split()))
    results.append(" ".join(map(str, stock_span(prices, N))))

# Xuất kết quả
print("\n".join(results))
