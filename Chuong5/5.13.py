import re

def evaluate_infix(expression):
    try:
        # Thay thế các phép chia để đảm bảo kết quả là số nguyên
        expression = re.sub(r'(?<=\d)/(\d+)', r'//\1', expression)
        return eval(expression)
    except Exception as e:
        return "Error"

# Nhập số lượng bộ test
T = int(input().strip())

if 1 <= T <= 100:
    results = []
    for _ in range(T):
        expression = input().strip()
        if 1 <= len(expression) <= 100:
            results.append(str(evaluate_infix(expression)))
    
    # Xuất kết quả
    print("\n".join(results))
