def normalize_expression(expression):
    stack = []
    result = []
    
    for char in expression:
        if char.isalpha():
            result.append(char)
        elif char == '(':
            stack.append(len(result))
        elif char == ')':
            if stack:
                start = stack.pop()
                result[start:] = ['('] + result[start:] + [')']
    
    return ''.join(result)

def are_expressions_equal(P1, P2):
    return normalize_expression(P1) == normalize_expression(P2)

# Nhập số lượng bộ test
T = int(input().strip())

if 1 <= T <= 100:
    results = []
    for _ in range(T):
        P1 = input().strip()
        P2 = input().strip()
        if 1 <= len(P1) <= 100 and 1 <= len(P2) <= 100:
            results.append("Yes" if are_expressions_equal(P1, P2) else "No")
    
    # Xuất kết quả
    print("\n".join(results))