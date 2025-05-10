def evaluate_prefix(expression):
    stack = []
    operators = {'+', '-', '*', '/'}
    
    for char in reversed(expression):
        if char.isdigit():
            stack.append(int(char))
        elif char in operators:
            if len(stack) >= 2:
                operand1 = stack.pop()
                operand2 = stack.pop()
                if char == '+':
                    stack.append(operand1 + operand2)
                elif char == '-':
                    stack.append(operand1 - operand2)
                elif char == '*':
                    stack.append(operand1 * operand2)
                elif char == '/':
                    stack.append(operand1 // operand2)  # Lấy phần nguyên
    
    return stack[0] if stack else 0

# Nhập số lượng bộ test
T = int(input().strip())

if 1 <= T <= 100:
    results = []
    for _ in range(T):
        expression = input().strip()
        if 2 <= len(expression) <= 20:
            results.append(str(evaluate_prefix(expression)))
    
    # Xuất kết quả
    print("\n".join(results))
