def longest_valid_parentheses(s):
    max_length = 0
    left = right = 0
    
    # Duyệt từ trái sang phải
    for char in s:
        if char == '(':
            left += 1
        else:
            right += 1
        
        if left == right:
            max_length = max(max_length, 2 * right)
        elif right > left:
            left = right = 0  # Reset khi số ')' nhiều hơn '('

    left = right = 0
    
    # Duyệt từ phải sang trái
    for char in reversed(s):
        if char == ')':
            right += 1
        else:
            left += 1
        
        if left == right:
            max_length = max(max_length, 2 * left)
        elif left > right:
            left = right = 0  # Reset khi số '(' nhiều hơn ')'

    return max_length

# Đọc input và xử lý từng test case
T = int(input().strip())

results = []
for _ in range(T):
    S = input().strip()
    results.append(str(longest_valid_parentheses(S)))

# Xuất kết quả
print("\n".join(results))
