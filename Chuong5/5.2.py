def min_bracket_reversals(s):
    if len(s) % 2 != 0:
        return -1  # Không thể tạo thành dãy ngoặc đúng nếu độ dài lẻ
    
    open_count = 0
    close_count = 0
    
    for char in s:
        if char == '(':
            open_count += 1
        else:
            if open_count > 0:
                open_count -= 1
            else:
                close_count += 1
    
    return (open_count + 1) // 2 + (close_count + 1) // 2

# Nhập số lượng bộ test
T = int(input().strip())

if 1 <= T <= 20:
    results = []
    for _ in range(T):
        s = input().strip()
        if 2 <= len(s) <= 100000 and len(s) % 2 == 0:
            results.append(str(min_bracket_reversals(s)))
    
    # Xuất kết quả
    print("\n".join(results))