def is_valid_number(n):
    """Kiểm tra xem số n có thỏa mãn điều kiện hay không"""
    digits = str(n)
    seen = set()
    
    for digit in digits:
        if digit > '5':  # Nếu có chữ số > 5 thì không hợp lệ
            return False
        if digit in seen:  # Nếu có chữ số lặp lại thì không hợp lệ
            return False
        seen.add(digit)
    
    return True

def count_valid_numbers(L, R):
    """Đếm số lượng số hợp lệ trong đoạn [L, R]"""
    count = 0
    for num in range(L, R + 1):
        if is_valid_number(num):
            count += 1
    return count

# Đọc input và xử lý
T = int(input())  # Số lượng test case
for _ in range(T):
    L, R = map(int, input().split())
    print(count_valid_numbers(L, R))
