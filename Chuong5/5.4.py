from itertools import combinations

def find_parentheses_pairs(expression):
    stack = []
    pairs = []
    
    for i, char in enumerate(expression):
        if char == '(':
            stack.append(i)
        elif char == ')':
            if stack:
                pairs.append((stack.pop(), i))
    
    return pairs

def generate_valid_expressions(expression, pairs):
    results = set()
    n = len(pairs)
    
    for r in range(1, n + 1):
        for combination in combinations(pairs, r):
            indexes_to_remove = set()
            for pair in combination:
                indexes_to_remove.update(pair)
            
            new_expr = ''.join(
                expression[i] for i in range(len(expression)) if i not in indexes_to_remove
            )
            results.add(new_expr)
    
    return sorted(results)

# Nhập biểu thức từ người dùng
expression = input().strip()

pairs = find_parentheses_pairs(expression)
valid_expressions = generate_valid_expressions(expression, pairs)

# In kết quả
print("\n".join(valid_expressions))