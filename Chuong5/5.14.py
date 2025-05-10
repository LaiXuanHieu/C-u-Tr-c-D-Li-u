def find_min_number(pattern):
    stack = []
    result = ""
    num = 1
    
    for char in pattern:
        stack.append(num)
        num += 1
        if char == 'I':
            while stack:
                result += str(stack.pop())
    
    stack.append(num)
    while stack:
        result += str(stack.pop())
    
    return result

# Nhập số lượng bộ test
T = int(input().strip())

if 1 <= T <= 100:
    results = []
    for _ in range(T):
        S = input().strip()
        if 1 <= len(S) <= 8:
            results.append(find_min_number(S))
    
    # Xuất kết quả
    print("\n".join(results))
