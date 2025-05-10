def max_valid_parentheses_length(P):
    stack = []
    valid_lengths = [0] * len(P)  # Mảng đánh dấu đoạn đúng
    
    # Duyệt qua xâu để tìm các đoạn đúng
    for i, char in enumerate(P):
        if char == '(':
            stack.append(i)
        elif char == ')' and stack:
            open_index = stack.pop()  # Lấy vị trí '(' phù hợp
            valid_lengths[open_index] = valid_lengths[i] = 1  # Đánh dấu phần tử hợp lệ
    
    # Tính tổng độ dài của tất cả các đoạn đúng
    max_length = 0
    current_length = 0
    for v in valid_lengths:
        if v == 1:
            current_length += 1
        else:
            max_length += current_length if current_length >= 2 else 0
            current_length = 0

    # Cộng nốt nếu còn đoạn đúng cuối cùng
    if current_length >= 2:
        max_length += current_length

    return max_length

# Đọc input và xử lý từng test case
T = int(input().strip())
results = []
for _ in range(T):
    P = input().strip()
    results.append(str(max_valid_parentheses_length(P)))

# Xuất kết quả
print("\n".join(results))
