def remove_brackets(expression):
    stack = []
    result = []
    sign = [1]  # Dùng để lưu trạng thái dấu hiện tại
    
    for char in expression:
        if char == '(':
            if result and result[-1] == '-':
                sign.append(-sign[-1])  # Đảo dấu nếu có dấu trừ phía trước
            else:
                sign.append(sign[-1])
        elif char == ')':
            sign.pop()
        elif char == '+':
            if result and result[-1] in "-+":
                result.pop()
            result.append('+' if sign[-1] == 1 else '-')
        elif char == '-':
            if result and result[-1] in "-+":
                result.pop()
            result.append('-' if sign[-1] == 1 else '+')
        else:
            result.append(char)
    
    return "".join(result)

# Nhập số lượng bộ test
T = int(input().strip())

if 1 <= T <= 100:
    results = []
    for _ in range(T):
        expression = input().strip()
        if 1 <= len(expression) <= 1000:
            results.append(remove_brackets(expression))
    
    # Xuất kết quả
    print("\n".join(results))