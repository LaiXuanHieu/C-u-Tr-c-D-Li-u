def prefix_to_infix(expression):
    stack = []
    operators = set(['+', '-', '*', '/', '^'])
    
    for char in reversed(expression):
        if char.isalnum():
            stack.append(char)
        elif char in operators:
            if len(stack) >= 2:
                operand1 = stack.pop()
                operand2 = stack.pop()
                new_expr = f'({operand1}{char}{operand2})'
                stack.append(new_expr)
    
    return stack[0] if stack else ""

# Nhập số lượng bộ test
T = int(input().strip())

if 1 <= T <= 100:
    results = []
    for _ in range(T):
        expression = input().strip()
        if 2 <= len(expression) <= 10**6:
            results.append(prefix_to_infix(expression))
    
    # Xuất kết quả
    print("\n".join(results))